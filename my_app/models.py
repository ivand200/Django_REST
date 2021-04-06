from django.db import models


class SP500(models.Model):
    symbol = models.CharField(max_length=30)
    name = models.TextField(max_length=50)
    momentum = models.FloatField(max_length=20)
# Create your models here.
