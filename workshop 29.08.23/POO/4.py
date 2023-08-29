# Herança de Formas Geométricas Crie uma classe base chamada FormaGeometrica com um método para calcular a área. Em seguida, crie subclasses como Retangulo e Circulo que herdam de FormaGeometrica e implementam seus próprios métodos para calcular a área.
# ??

class FormaGeometrica:
    def area(self):
        return self.largura * self.altura

class Retangulo(FormaGeometrica):
    def area(self, largura, altura):
        self.largura = largura
        self.altura = altura
        return largura * altura

class Circulo(FormaGeometrica):
    def area(self, raio):
        self.raio = raio
        return 3.14159 * raio ** 2 #pi

retangulo = Retangulo()
circulo = Circulo()

largura = 2
altura = 5
raio = 3

print("Área do RETÂNGULO:", retangulo.area(largura, altura))
print("Área do CÍRCULO:", circulo.area(raio))