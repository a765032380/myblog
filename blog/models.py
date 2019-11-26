from django.db import models

# Create your models here.

from django.db import models


class Test(models.Model):
    title = models.CharField(max_length=20)
    context = models.TextField()
