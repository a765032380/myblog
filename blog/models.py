from django.db import models

# Create your models here.

from django.db import models


class Test(models.Model):
    title = models.CharField(max_length=20)
    context = models.TextField()


class User(models.Model):
    name = models.CharField(max_length=20)
    phone = models.CharField(max_length=11)
    age = models.CharField(max_length=3)