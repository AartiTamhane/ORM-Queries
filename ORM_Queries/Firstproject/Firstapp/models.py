from django.db import models

# Create your models here.
class Student(models.Model):
    rn = models.IntegerField()
    name = models.CharField(max_length=20)
    marks = models.FloatField()
   # mail = models.EmailField(max_length=254)

    def __str__(self):
        return f'{self.rn},{self.name},{self.marks}'

class Employee(models.Model):
    eid = models.IntegerField()
    ename = models.CharField(max_length=32)

