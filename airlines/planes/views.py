from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response

from math import log

from .models import Passenger, Plane
from .serializers import PlaneSerializer, PassengerSerializer

CAPACITY_MULTIPLIER = 200
CONSUMPTION_MULTIPLIER = 0.8
CONSUMPTION_PASS_MULTIPLIER = 0.002

class PlaneViewSet(viewsets.ModelViewSet):
    serializer_class = PlaneSerializer
    queryset = Plane.objects.all()

    def perform_create(self, serializer):
        request = serializer.context['request']
        id = request.data["id"]
        tank_capacity = CAPACITY_MULTIPLIER * id
        passengers_count = Passenger.objects.filter(plane__id=id).count()
        consumption = (CONSUMPTION_MULTIPLIER * log(id)) + (CONSUMPTION_PASS_MULTIPLIER * passengers_count)
        serializer.save(id=id, tank_capacity=tank_capacity, consumption=consumption) 


class PassengerViewSet(viewsets.ModelViewSet):
    serializer_class = PassengerSerializer
    queryset = Passenger.objects.all()


