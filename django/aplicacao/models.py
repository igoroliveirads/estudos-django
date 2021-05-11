from django.db import models


class Product(models.Model):
    name = models.CharField('Nome', max_length=100)
    price = models.DecimalField('Preço', decimal_places=2, max_digits=8)
    stock = models.IntegerField('Estoque')

    # define como será apresentada a classe
    def __str__(self):
        return self.name


class Client(models.Model):
    name = models.CharField('Nome', max_length=100)
    surname = models.CharField('Sobrenome', max_length=100)
    email = models.EmailField('Email', max_length=100)

    def __str__(self):
        return f'{self.name} {self.surname}'
