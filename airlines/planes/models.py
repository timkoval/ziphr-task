from django.db import models
import uuid 
from django.db.models.deletion import CASCADE

class Plane(models.Model):
    id = models.AutoField(primary_key=True)
    tank_capacity = models.PositiveIntegerField(verbose_name='Fuel Tank Capacity')
    consumption = models.PositiveIntegerField()

class Passenger(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    plane = models.ForeignKey(Plane, on_delete=CASCADE)


    

