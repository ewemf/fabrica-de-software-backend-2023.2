from django.db import models

class Pessoa(models.Model):
    nome = models.CharField(max_length=20)

    def __str__(self):
        return f'Nome: {self.nome}'

class ToDoList(models.Model):
    tarefa = models.CharField(max_length = 20)
    choices_status = [
        ('Pronto', 'Pronto'),
        ('Em Andamento', 'Em Andamento'),
        ('Pendente', 'Pendente'),
    ]
    status = models.CharField(choices=choices_status, max_length=12)
    pessoa = models.ForeignKey(
        Pessoa,
        max_length=20,
        on_delete=models.CASCADE
    )
