from django.db import models

# Create your models here.
from diary.metadata import standards as std


class User(models.Model):
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phoneNum = models.CharField(max_length=100)
    country = models.CharField(max_length=100, choices=std.Country)
    language = models.CharField(max_length=100, choices=std.Language)
    createdAt = models.DateTimeField()
    updatedAt = models.DateTimeField()
    deletedAt = models.DateTimeField()
    agreedAt = models.DateTimeField()

    def __str__(self):
        return self.name


class