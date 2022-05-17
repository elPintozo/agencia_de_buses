from dataclasses import fields
from rest_framework import serializers

from apps.flota import models

class ChauffeurSerializersCreate(serializers.ModelSerializer):
    class Meta:
        model = models.Chauffeur
        fields = ['dni',]

class ChauffeurSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Chauffeur
        fields = '__all__'

class BusSerializersCreate(serializers.ModelSerializer):
    class Meta:
        model = models.Bus
        fields = ['plate',]

class BusSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Bus
        fields = '__all__'

class RouteSerializersCreate(serializers.ModelSerializer):
    class Meta:
        model = models.Route
        fields = ['name',]

class RouteSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Route
        fields = '__all__'

class ScheduleSerializersCreate(serializers.ModelSerializer):
    class Meta:
        model = models.Schedule
        fields = ['origin_date', 'destination_date',]

class ScheduleSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Schedule
        fields = '__all__'

class BusRouteSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.BusRoute
        fields = '__all__'