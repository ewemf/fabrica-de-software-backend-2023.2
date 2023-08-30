# Classe Conta Bancária Crie uma classe chamada ContaBancaria que tenha atributos como titular, saldo e métodos para depositar e sacar dinheiro.

class ContaBancária ():
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def mostrar_saldo(self):
        print(f'Seu saldo é: {self.saldo}')
    def depositar(self, dinheiro):
        self.saldo += dinheiro
    
    def sacar_dinheiro(self, valor):
        if valor > self.saldo:
            print('voce nao pode sacar.')
        else:
            self.saldo -= valor

guilherme = ContaBancária('guilherme', 0)
guilherme.depositar(50)
guilherme.mostrar_saldo()

guilherme.sacar_dinheiro(20)
guilherme.mostrar_saldo()
