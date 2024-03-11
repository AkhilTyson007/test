from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    email = models.EmailField(max_length=254,unique=True)
    mobile = models.IntegerField(unique=True)

    def __str__(self):
        return str(self.id) + " - " + self.name

class Employee(models.Model):
    empID = models.CharField(max_length=50, unique=True, primary_key=True)
    #name = models.CharField(max_length=50)
    mobile = models.BigIntegerField()
    uid = models.OneToOneField(User, on_delete=models.CASCADE)

