from django.db import models

class Autor(models.Model):
    nome = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.nome}'
    
class Biblioteca(models.Model):
    livro = models.CharField(max_length=20)
    preço = models.FloatField(default=0)
    autor = models.ForeignKey(
        Autor,
        max_length=20,
        on_delete=models.CASCADE
    )