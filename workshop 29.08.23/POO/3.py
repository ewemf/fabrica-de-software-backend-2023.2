#Classe Carro Crie uma classe chamada Carro com atributos como marca, modelo e ano. Crie um método para acelerar o carro.

class Carro():
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
    
    def carro(self):
        print (f'MARCA DO CARRO: {self.marca}, MODELO: {self.modelo}, ANO: {self.ano}.')

carro = Carro('Hyundai HB20', 'Comfort Automático', 2023)
carro.carro()
