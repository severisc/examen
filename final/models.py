from django.shortcuts import render
from django.db import models

# Create your models here.

class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    number_of_login = models.IntegerField()

    class Meta:
        db_table = "user"

    def __str__(self):
        return self.last_name
