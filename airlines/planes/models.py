from django.db import models
import uuid 
from django.db.models.deletion import CASCADE

class Plane(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    tank_capacity = models.PositiveIntegerField(verbose_name='Fuel Tank Capacity')
    consumption = models.PositiveIntegerField()

class Passenger(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    plane = models.ForeignKey(Plane, on_delete=CASCADE)


    

