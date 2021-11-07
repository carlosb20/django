from django.db import models

class Prpdutos(models.Model):
    nome = models.CharField('nome',max_length=100)
    preco = models.DecimalField('preco',decimal_places=2,max_digits=8)
    estoque = models.IntegerField('Quatidade em estoque')

    def __str__(self):
        return self.nome

class Cliente(models.Model):
    nome = models.CharField('nome',max_length=100)
    sobrenome = models.CharField('sobrenome',max_length=100)
    email = models.EmailField('Email',max_length=100)

    def __str__(self):
        return f'{self.nome} {self.sobrenome}'

