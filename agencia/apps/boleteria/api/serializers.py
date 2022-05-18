from rest_framework import serializers

from apps.boleteria import models

class PassengerSerializers(serializers.ModelSerializer):
    create_date = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    class Meta:
        model = models.Passenger
        fields = '__all__'

class TicketSerializers(serializers.ModelSerializer):
    create_date = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    class Meta:
        model = models.Ticket
        fields = '__all__'

