from django.db import models

# Create your models here.
from django.db import models
class Employees(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=25)
    age = models.IntegerField()
    skill=models.CharField(max_length=50)
    hireDate = models.DateField(null=True,blank=True)

class Skill(models.Model):
    skill = models.CharField(max_length=50)
    
# Create your models here.