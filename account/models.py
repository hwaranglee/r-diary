from django.db import models
from diary.metadata import standards


# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=254)
    password = models.CharField(min_length=6, max_length=200)
    birth = models.DateField()
    createdAt = models.DateTimeField()
    updatedAt = models.DateTimeField(auto_now=True)
    deletedAt = models.DateTimeField()
    agreedAt = models.DateTimeField()
    passUpdatedAt = models.DateTimeField()
    isVerifiedEmail = models.BooleanField(default=True)
    country = models.CharField(max_length=4, choices=standards.Country.choices)
    language = models.CharField(max_length=4, choices=standards.Language.choices)

    def __str__(self):
        return self.email


class LoginHistory(models.Model):
    userId = models.ForeignKey(User.id)
    type = models.CharField(max_length=10, choices=standards.AccountType.choices)
    platform = models.CharField(max_length=1000)
    device = models.CharField(max_length=1000)
    browser = models.CharField(max_length=1000)
    version = models.CharField(max_length=1000)
    token = models.CharField(max_length=1000)
    ip = models.IPAddressField()
    createdAt = models.DateTimeField()
    updatedAt = models.DateTimeField()

    def __str__(self):
        return '{self.userId} : {self.type}'


class Auth(models.Model):
    createdAt = models.DateTimeField()
    key = models.CharField(max_length=100)
    token = models.CharField(max_length=1000)
    type = models.CharField(max_length=10, choices=standards.AccountType.choices)

    def __str__(self):
        return '{self.type} : {self.key} : {self.token}'
