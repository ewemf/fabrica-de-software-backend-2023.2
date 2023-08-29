# Classe Conta Bancária Crie uma classe chamada ContaBancaria que tenha atributos como titular, saldo e métodos para depositar e sacar dinheiro.

class ContaBancária ():
    def __init__(self, titular, saldo, metodosDep, metodosSac):
        self.titular = titular
        self.saldo = saldo
        self.metodosDep = metodosDep
        self.metodosSac = metodosSac
    
    def contabancaria(self):
        print (f'Titular: {self.titular}; SALDO: {self.saldo}; Método para depositar dinheiro: {self.metodosDep}; Método para sacar dinheiro: {self.metodosSac}.')

pessoa = ContaBancária('Ewellyn', 200, 'Depósito Bancário', 'Saque Digital')
pessoa.contabancaria()
