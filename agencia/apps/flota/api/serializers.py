from dataclasses import fields
from rest_framework import serializers

from apps.flota import models

class ChauffeurSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Chauffeur
        fields = '__all__'

class BusSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Bus
        fields = '__all__'

class RouteSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Route
        fields = '__all__'

class ScheduleSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Schedule
        fields = '__all__'

class BusRouteSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.BusRoute
        fields = '__all__'