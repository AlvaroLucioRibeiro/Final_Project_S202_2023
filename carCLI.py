from car import Carro, Motor
from database import Database

# Classe base para a interface de linha de comando
class SimpleCLI:
    def __init__(self):
        self.commands = {}  # Dicionário para armazenar comandos

    # Método para adicionar um comando ao dicionário
    def add_command(self, name, function):
        self.commands[name] = function

    # Método para executar a interface de linha de comando
    def run(self):
        while True:
            command = input("Enter a command: ")
            if command == "quit":
                print("Goodbye!")
                break
            elif command in self.commands:
                self.commands[command]()
            else:
                print("Invalid command. Try again.")

# Classe para a interface de linha de comando específica para carros
class CarCLI(SimpleCLI):
    def __init__(self, car_crud, concessionaria):
        super().__init__()
        self.car_crud = car_crud  # Instância da classe CarCRUD
        self.concessionaria = concessionaria  # Instância da classe Concessionaria
        # Adicionando comandos específicos para carros
        self.add_command("create", self.create_car)
        self.add_command("read", self.read_car)
        self.add_command("update", self.update_car)
        self.add_command("delete", self.delete_car)

    # Método para criar um carro
    def create_car(self):
        # Solicitando informações do carro ao usuário
        marca = input("Enter the car's brand: ")
        modelo = input("Enter the car's model: ")
        ano = int(input("Enter the car's year: "))
        preco = float(input("Enter the car's price: "))
        cor = input("Enter the car's color: ")
        tipo = input("Enter the motor's type: ")
        potencia = int(input("Enter the motor's power: "))
        cavalos = int(input("Enter the motor's horsepower: "))
        combustivel = input("Enter the motor's fuel type: ")
        
        # Criando instâncias de Motor e Carro
        motor = Motor(tipo, potencia, cavalos, combustivel)
        car = Carro(marca, modelo, ano, preco, cor, motor)
        
        # Adicionando o relacionamento com a concessionária
        car.concessionaria = self.concessionaria

        # Chamando o método create da classe CarCRUD
        self.car_crud.create(car)

    # Método para ler as informações de um carro
    def read_car(self):
        # Solicitando a marca e o modelo do carro ao usuário
        marca = input("Enter the car's brand: ")
        modelo = input("Enter the car's model: ")
        # Chamando o método read da classe CarCRUD
        car = self.car_crud.read(marca, modelo)
        if car:
            car.descricao()  # Imprimindo a descrição do carro se ele for encontrado
        else:
            print("Car not found.")

    # Método para atualizar as informações de um carro
    def update_car(self):
        # Solicitando a marca e o modelo do carro ao usuário
        marca = input("Enter the car's brand: ")
        modelo = input("Enter the car's model: ")
        # Chamando o método read da classe CarCRUD para encontrar o carro
        car = self.car_crud.read(marca, modelo)

        if car:
            print("Car found - CLI.")
            # Solicitando as novas informações do carro ao usuário
            novo_modelo = input("Enter the car's new model: ")
            novo_ano = input("Enter the car's new year: ")
            novo_preco = input("Enter the car's new price: ")
            nova_cor = input("Enter the car's new color: ")
            novo_tipo = input("Enter the motor's new type: ")
            nova_potencia = input("Enter the motor's new power: ")
            novos_cavalos = input("Enter the motor's new horsepower: ")
            novo_combustivel = input("Enter the motor's new fuel type: ")

            # Atualizando as informações do carro
            car.modelo = novo_modelo if novo_modelo else car.modelo
            car.ano = int(novo_ano) if novo_ano else car.ano
            car.preco = float(novo_preco) if novo_preco else car.preco
            car.cor = nova_cor if nova_cor else car.cor
            car.motor.tipo = novo_tipo if novo_tipo else car.motor.tipo
            car.motor.potencia = int(nova_potencia) if nova_potencia else car.motor.potencia
            car.motor.cavalos = int(novos_cavalos) if novos_cavalos else car.motor.cavalos
            car.motor.combustivel = novo_combustivel if novo_combustivel else car.motor.combustivel

            # Chamando o método update da classe CarCRUD para atualizar o carro no banco de dados
            self.car_crud.update(marca, modelo, car)  # Passar a marca e o modelo originais junto com o carro atualizado
            print("Car updated successfully.")
        else:
            print("Car not found - CLI.")

    # Método para deletar um carro
    def delete_car(self):
        # Solicitando a marca e o modelo do carro ao usuário
        marca = input("Enter the car's brand: ")
        modelo = input("Enter the car's model: ")
        # Chamando o método read da classe CarCRUD para encontrar o carro
        car = self.car_crud.read(marca, modelo)
        
        if car:
            # Chamando o método delete da classe CarCRUD para deletar o carro do banco de dados
            self.car_crud.delete(car.marca, car.modelo)
            print("Car deleted successfully.")
        else:
            print("Car not found.")

    # Método para executar a interface de linha de comando específica para carros
    def run(self):
        print("Welcome to Mr. Dito's Dealership - Administrator Panel")
        print("To proceed, please enter a command:")
        print("create, read, update, delete, quit")
        super().run()