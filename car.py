# Classe que representa um motor
class Motor:
    def __init__(self, tipo, potencia, cavalos, combustivel):
        self.tipo = tipo
        self.potencia = potencia
        self.cavalos = cavalos
        self.combustivel = combustivel

# Classe que representa um carro
class Carro:
    def __init__(self, marca, modelo, ano, preco, cor, motor):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.preco = preco
        self.cor = cor
        self.motor = motor

    # Método para imprimir a descrição do carro
    def descricao(self):
        print(f"Marca: {self.marca}, Ano: {self.ano}, Preço: {self.preco}, Cor: {self.cor}")
        print(f"Motor: {self.motor.tipo}, Potência: {self.motor.potencia}, Cavalos: {self.motor.cavalos}, Combustível: {self.motor.combustivel}")

# Classe que representa a Concessionária
class Concessionaria:
    def __init__(self, nome):
        self.nome = nome
