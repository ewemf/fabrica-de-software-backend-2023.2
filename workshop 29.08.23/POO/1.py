#Classe Pessoa Crie uma classe chamada Pessoa que tenha atributos como nome, idade e profissão. Crie um método que imprima uma saudação com as informações da pessoa.

class Pessoa():
    def __init__(self, nome, idade, profissao):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao
    
    def saudacao(self):
        print (f'Oi, meu nome é {self.nome}, tenho {self.idade} anos e sou {self.profissao}.')

pedro = Pessoa('Pedro', 25, 'Reporter')
pedro.saudacao()

guilherme = Pessoa('Guilherme', 18, 'Estudante')
guilherme.saudacao()

ewe = Pessoa('Ewellyn', 18, 'Estudante')
ewe.saudacao()
