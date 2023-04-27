from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Programmer(models.Model):
    name = models.CharField(max_length=20)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class User(models.Model):
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=15)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=40)