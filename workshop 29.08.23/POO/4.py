# Herança de Formas Geométricas Crie uma classe base chamada FormaGeometrica com um método para calcular a área. Em seguida, crie subclasses como Retangulo e Circulo que herdam de FormaGeometrica e implementam seus próprios métodos para calcular a área.
# ??

class FormaGeometrica:
    def calcular_a_area(self, raio):
        return 3.14*(raio**2)

class Circulo(FormaGeometrica):
    pass

class Retangulo(FormaGeometrica):
    def calcular_a_area(self, base, altura):
        return base*altura

circulo = Circulo()
area = circulo.calcular_a_area(5)
print(area)

retangulo = Retangulo()
area = retangulo.calcular_a_area(5, 10)
print(area)

# EXEMPLO FEITO NA SALA:

class Garrafa:
    def __init__(self, tamanho, cor, marca):
        self.tamanho = tamanho
        self.cor = cor
        self.marca = marca

    def __str__(self):
        return f'tamanho: {self.tamanho}, marca: {self.marca}'

class GarrafaDeVidro(Garrafa):
    def quebrar(self):
        print('crack')

garrafa = Garrafa(200, 'preto', 'Stanley')

garrafa_de_vidro = GarrafaDeVidro(200, 'transparente', 'vidro')

a = garrafa.__str__()
print(a)
print(garrafa_de_vidro.__str__())
