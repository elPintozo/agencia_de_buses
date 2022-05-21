import uuid
from django.db import models
from django.db.models.signals import pre_save

class Chauffeur(models.Model):
    chauffeur_id = models.CharField(max_length=100, null=False, blank=False, unique=True)
    dni = models.CharField(max_length=12, null=False)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.dni

class Bus(models.Model):
    bus_id = models.CharField(max_length=100, null=False, blank=False, unique=True)
    plate = models.CharField(max_length=6, null=False)# str -> LLLLNN
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.plate

class Route(models.Model):
    route_id = models.CharField(max_length=100, null=False, blank=False, unique=True)
    name = models.CharField(max_length=255, null=False)# str-str -> origin-destination
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Schedule(models.Model):
    schedule_id = models.CharField(max_length=100, null=False, blank=False, unique=True)
    origin_date = models.DateTimeField()
    destination_date = models.DateTimeField()
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Origin:{self.origin_date} | Destination:{self.destination_date}"


class BusRoute(models.Model):
    route = models.ForeignKey(Route, on_delete=models.CASCADE, null=True)
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE, null=True)
    chauffeur = models.ForeignKey(Chauffeur, on_delete=models.CASCADE, null=True)
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE, null=True)
    create_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = [['route', 'bus', 'chauffeur', 'schedule']]
    
    def __str__(self):
        return f"Route: {self.route}"
    
    def remove_bus_association(bus: Bus):
        """Function that remove association between Bus and BusRoute model"""
        
        list_association = BusRoute.objects.filter(bus=bus)
        for association in list_association:
            association.bus = None
            association.save()


def set_chauffeur_id(sender, instance, *args, **kwargs):
    if not instance.chauffeur_id:
        instance.chauffeur_id = str(uuid.uuid4())[0:8]

def set_bus_id(sender, instance, *args, **kwargs):
    if not instance.bus_id:
        instance.bus_id = str(uuid.uuid4())[0:8]

def set_route_id(sender, instance, *args, **kwargs):
    if not instance.route_id:
        instance.route_id = str(uuid.uuid4())[0:8]

def set_schedule_id(sender, instance, *args, **kwargs):
    if not instance.schedule_id:
        instance.schedule_id = str(uuid.uuid4())[0:8]

pre_save.connect(set_chauffeur_id, sender=Chauffeur)
pre_save.connect(set_bus_id, sender=Bus)
pre_save.connect(set_route_id, sender=Route)
pre_save.connect(set_schedule_id, sender=Schedule)
