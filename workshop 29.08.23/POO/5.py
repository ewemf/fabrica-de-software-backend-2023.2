# polimorfism Crie uma classe base chamada Animal com métodos para emitir um som e mostrar informações gerais. Crie subclasses como Cachorro e Gato que herdam de Animal e implementam seus próprios métodos para emitir sons específicos.

class Animal:
    def emitir_som(self):
        pass
    
    def info_gerais(self):
        pass

class Cachorro(Animal):
    def emitir_som(self):
        return "O cachorro faz 'au au'"
    
    def info_gerais(self):
        return "Cachorro: Animal doméstico fiel e leal"

class Gato(Animal):
    def emitir_som(self):
        return "O gato faz 'miau'"
    
    def info_gerais(self):
        return "Gato: Animal independente e carinhoso"

animais = [Cachorro(), Gato()]

for animal in animais:
    print(animal.emitir_som())
    print(animal.info_gerais())