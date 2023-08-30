# polimorfism Crie uma classe base chamada Animal com métodos para emitir um som e mostrar informações gerais. Crie subclasses como Cachorro e Gato que herdam de Animal e implementam seus próprios métodos para emitir sons específicos.

class Animal:
    def som(self):
        pass
    
    def info(self):
        pass

class Cachorro(Animal):
    def som(self):
        return "Som emitido pelo CACHORRO: 'AU AU'"
    
    def info(self):
        return "Informações gerais do CACHORRO: Animal doméstico fiel e amoroso"

class Gato(Animal):
    def som(self):
        return "Som emitido pelo GATO: 'MIAU'"
    
    def info(self):
        return "Informações gerais do GATO: Animal independente e carinhoso"

animais = [Cachorro(), Gato()]

for animal in animais:
    print(animal.som())
    print(animal.info())
