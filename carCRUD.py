from car import Carro, Motor

# Classe para realizar operações CRUD (Create, Read, Update, Delete) em carros
class CarCRUD:
    def __init__(self, database):
        self.db = database

    # Método para criar um carro no banco de dados
    def create(self, car):
        # Query para criar um carro e um motor no banco de dados
        query_concessionaria = "MATCH (con:Concessionaria {nome: 'Consessionária Sr. Dito'})"
        query = query_concessionaria + " CREATE (con)<-[:PERTENCE]-(c:Car {marca: $marca, modelo: $modelo, ano: $ano, preco: $preco, cor: $cor})-[:TEM]->(m:Motor {tipo: $tipo, potencia: $potencia, cavalos: $cavalos, combustivel: $combustivel})"
        parameters = {"marca": car.marca, "modelo": car.modelo, "ano": car.ano, "preco": car.preco, "cor": car.cor,
                      "tipo": car.motor.tipo, "potencia": car.motor.potencia, "cavalos": car.motor.cavalos, "combustivel": car.motor.combustivel}
        self.db.execute_query(query, parameters)

    # Método para ler um carro do banco de dados
    def read(self, marca, modelo):
        # Query para encontrar um carro e seu motor no banco de dados
        query = "MATCH (c:Car {marca: $marca, modelo: $modelo})-[:TEM]->(m:Motor) RETURN c.marca, c.modelo, c.ano, c.preco, c.cor, m.tipo, m.potencia, m.cavalos, m.combustivel"
        parameters = {"marca": marca, "modelo": modelo}
        result = self.db.execute_query(query, parameters)
        
        # Se o resultado não for vazio, criar um objeto Carro e retornar
        if result:
            record = result[0]
            motor = Motor(record['m.tipo'], record['m.potencia'], record['m.cavalos'], record['m.combustivel'])
            return Carro(record['c.marca'], record['c.modelo'], record['c.ano'], record['c.preco'], record['c.cor'], motor)
        else:
            return None

    # Método para atualizar um carro no banco de dados
    def update(self, marca, modelo, car):
        # Primeiro, encontre o carro
        find_query = "MATCH (c:Car {marca: $marca, modelo: $modelo})-[:TEM]->(m:Motor) RETURN c, m"
        find_parameters = {"marca": marca, "modelo": modelo}
        result = self.db.execute_query(find_query, find_parameters)

        # Se o carro foi encontrado, atualize seus atributos
        if result:
            print("Car found - CRUD.")
            update_query = "MATCH (c:Car {marca: $marca, modelo: $modelo})-[:TEM]->(m:Motor) SET c.modelo = $novo_modelo, c.ano = $ano, c.preco = $preco, c.cor = $cor, m.tipo = $tipo, m.potencia = $potencia, m.cavalos = $cavalos, m.combustivel = $combustivel"
            update_parameters = {"marca": marca, "modelo": modelo, "novo_modelo": car.modelo, "ano": car.ano, "preco": car.preco, "cor": car.cor, "tipo": car.motor.tipo, "potencia": car.motor.potencia, "cavalos": car.motor.cavalos, "combustivel": car.motor.combustivel}
            self.db.execute_query(update_query, update_parameters)
        else:
            print("Car not found - CRUD.")

   # Método para deletar um carro do banco de dados
    def delete(self, marca, modelo):
        # First, find the car node
        find_car_query = """
        MATCH (c:Car {marca: $marca, modelo: $modelo})-[t:TEM]->(m:Motor)
        RETURN c, t, m
        """
        find_car_parameters = {"marca": marca, "modelo": modelo}
        result = self.db.execute_query(find_car_query, find_car_parameters)

        if result:
            if len(result) > 0:
                car = result[0]['c']
                
                # Next, find and delete the motor node
                delete_motor_query = """
                MATCH (c:Car {marca: $marca, modelo: $modelo})-[t:TEM]->(m:Motor) DELETE t, m
                """
                self.db.execute_query(delete_motor_query, find_car_parameters)

                # Finally, delete the car node
                delete_car_query = """
                MATCH (c:Car {marca: $marca, modelo: $modelo})-[t:PERTENCE]->(m:Concessionaria) DELETE t, c
                """
                self.db.execute_query(delete_car_query, find_car_parameters)

                print("Car deleted successfully.")
            else:
                print("Car not found.")
        else:
            print("Car not found.")