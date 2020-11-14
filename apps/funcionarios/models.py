from django.db import models
from django.contrib.auth.models import User 
from apps.departamentos.models import Departamento


# Create your models here.

class Funcionario(models.Model):
    nome = models.CharField(max_length=100, help_text='Nome do Funcionario')
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    departamento = models.ManyToManyField(Departamento)
    def __str__(self):
        return self.nome
