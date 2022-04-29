from rest_framework import serializers
from .models import Plane, Passenger

class PlaneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plane
        fields = "__all__"

class PlaneIdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plane
        fields = ["id"]

class PassengerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passenger
        fields = "__all__"
