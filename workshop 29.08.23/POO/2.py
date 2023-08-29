# Classe Conta Bancária Crie uma classe chamada ContaBancaria que tenha atributos como titular, saldo e métodos para depositar e sacar dinheiro.

class ContaBancária ():
    def __init__(self, titular, saldo, metodosDep, metodosSac):
        self.titular = titular
        self.saldo = saldo
        self.metodosDep = metodosDep
        self.metodosSac = metodosSac
    
    def contabancaria(self):
        print (f'Oi, meu titular é {self.titular}, tenho {self.saldo} reais de saldo e esse é um dos métodos para depositar dinheiro: {self.metodosDep}; e esse para sacar dinheiro: {self.metodosSac}.')

pessoa = ContaBancária('Ewellyn', 200, 'Depósito', 'Saque')
pessoa.contabancaria()