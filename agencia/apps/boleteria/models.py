import uuid
from django.db import models
from django.db.models.signals import pre_save
from apps.flota.models import Route

class Passenger(models.Model):
    passenger_id = models.CharField(max_length=100, null=False, blank=False, unique=True)
    dni = models.CharField(max_length=12, null=False)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.dni

class Ticket(models.Model):
    ticket_id = models.CharField(max_length=100, null=False, blank=False, unique=True)
    seat_number = models.IntegerField()
    route = models.ForeignKey(Route, on_delete=models.CASCADE)
    passenger = models.ForeignKey(Passenger, on_delete=models.CASCADE)

    class Meta:
        unique_together = [['seat_number', 'route']]

def set_passenger_id(sender, instance, *args, **kwargs):
    if not instance.passenger_id:
        instance.passenger_id = str(uuid.uuid4())[0:8]

def set_ticket_id(sender, instance, *args, **kwargs):
    if not instance.ticket_id:
        instance.ticket_id = str(uuid.uuid4())[0:8]

pre_save.connect(set_passenger_id, sender=Passenger)
pre_save.connect(set_ticket_id, sender=Ticket)
