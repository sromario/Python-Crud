from django.db import models

# Create your models here.

class Alunos(models.Model):
    nome = models.CharField(max_length=150)
    unidade = models.CharField(max_length=100)
    idade =  models.IntegerField()