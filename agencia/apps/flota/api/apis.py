from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from apps.flota import models
from apps.flota.api import serializers

@api_view(['GET', 'POST'])
def chauffeur_api_view(request):

    # list
    if request.method == 'GET':
        chauffeurs = models.Chauffeur.objects.all()
        chauffeurs_serializers = serializers.ChauffeurSerializers(chauffeurs, many=True)
        return Response(chauffeurs_serializers.data, status=status.HTTP_200_OK)

    # create
    elif request.method == 'POST':
        chauffeurs_serializers = serializers.ChauffeurSerializersCreate(data=request.data)
        # validation
        if chauffeurs_serializers.is_valid():
            chauffeurs_serializers.save()
            return Response({'message':'Created'}, status=status.HTTP_201_CREATED)
        else:
            return Response(chauffeurs_serializers.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def chauffeur_detail_view(request, pk: int=None):

    # queryset
    chauffeur = models.Chauffeur.objects.filter(pk=pk).first()

    # validation
    if chauffeur:
        
        # retrieve
        if request.method == 'GET':
            chauffeur_serializers = serializers.ChauffeurSerializers(chauffeur)
            return Response(chauffeur_serializers.data, status=status.HTTP_200_OK)
        # update
        elif request.method == 'PUT':
            chauffeur_serializers = serializers.ChauffeurSerializers(chauffeur, data=request.data)
            if chauffeur_serializers.is_valid():
                chauffeur_serializers.save()
                return Response(chauffeur_serializers.data, status=status.HTTP_202_ACCEPTED)
            else:
                return Response(chauffeur_serializers.errors, status=status.HTTP_400_BAD_REQUEST)
        # delete
        elif request.method == 'DELETE':
            chauffeur.delete()
            return Response({'message':'Deleted'}, status=status.HTTP_202_ACCEPTED)
    
    else:
        return Response({'message':"Don't found"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def bus_api_view(request):

    # list
    if request.method == 'GET':
        buses = models.Bus.objects.all()
        buses_serializers = serializers.BusSerializers(buses, many=True)
        return Response(buses_serializers.data, status=status.HTTP_200_OK)

    # create
    elif request.method == 'POST':
        buses_serializers = serializers.BusSerializersCreate(data=request.data)
        # validation
        if buses_serializers.is_valid():
            buses_serializers.save()
            return Response({'message':'Created'}, status=status.HTTP_201_CREATED)
        else:
            return Response(buses_serializers.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def bus_detail_view(request, pk: int=None):

    # queryset
    bus = models.bus.objects.filter(pk=pk).first()

    # validation
    if bus:
        
        # retrieve
        if request.method == 'GET':
            bus_serializers = serializers.BusSerializers(bus)
            return Response(bus_serializers.data, status=status.HTTP_200_OK)
        # update
        elif request.method == 'PUT':
            bus_serializers = serializers.BusSerializers(bus, data=request.data)
            if bus_serializers.is_valid():
                bus_serializers.save()
                return Response(bus_serializers.data, status=status.HTTP_202_ACCEPTED)
            else:
                return Response(bus_serializers.errors, status=status.HTTP_400_BAD_REQUEST)
        # delete
        elif request.method == 'DELETE':
            bus.delete()
            return Response({'message':'Deleted'}, status=status.HTTP_202_ACCEPTED)
    
    else:
        return Response({'message':"Don't found"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def route_api_view(request):

    # list
    if request.method == 'GET':
        routes = models.Route.objects.all()
        routes_serializers = serializers.RouteSerializers(routes, many=True)
        return Response(routes_serializers.data, status=status.HTTP_200_OK)

    # create
    elif request.method == 'POST':
        routes_serializers = serializers.RouteSerializersCreate(data=request.data)
        # validation
        if routes_serializers.is_valid():
            routes_serializers.save()
            return Response({'message':'Created'}, status=status.HTTP_201_CREATED)
        else:
            return Response(routes_serializers.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def route_detail_view(request, pk: int=None):

    # queryset
    route = models.Route.objects.filter(pk=pk).first()

    # validation
    if route:
        
        # retrieve
        if request.method == 'GET':
            route_serializers = serializers.RouteSerializers(route)
            return Response(route_serializers.data, status=status.HTTP_200_OK)
        # update
        elif request.method == 'PUT':
            route_serializers = serializers.RouteSerializers(route, data=request.data)
            if route_serializers.is_valid():
                route_serializers.save()
                return Response(route_serializers.data, status=status.HTTP_202_ACCEPTED)
            else:
                return Response(route_serializers.errors, status=status.HTTP_400_BAD_REQUEST)
        # delete
        elif request.method == 'DELETE':
            route.delete()
            return Response({'message':'Deleted'}, status=status.HTTP_202_ACCEPTED)
    
    else:
        return Response({'message':"Don't found"}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def schedule_api_view(request):

    # list
    if request.method == 'GET':
        schedules = models.Schedule.objects.all()
        schedules_serializers = serializers.ScheduleSerializers(schedules, many=True)
        return Response(schedules_serializers.data, status=status.HTTP_200_OK)

    # create
    elif request.method == 'POST':
        schedule_serializers = serializers.ScheduleSerializersCreate(data=request.data)
        # validation
        if schedule_serializers.is_valid():
            schedule_serializers.save()
            return Response({'message':'Created'}, status=status.HTTP_201_CREATED)
        else:
            return Response(schedule_serializers.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def schedule_detail_view(request, pk: int=None):

    # queryset
    schedule = models.Schedule.objects.filter(pk=pk).first()

    # validation
    if schedule:
        
        # retrieve
        if request.method == 'GET':
            schedule_serializers = serializers.ScheduleSerializers(schedule)
            return Response(schedule_serializers.data, status=status.HTTP_200_OK)
        # update
        elif request.method == 'PUT':
            schedule_serializers = serializers.ScheduleSerializers(schedule, data=request.data)
            if schedule_serializers.is_valid():
                schedule_serializers.save()
                return Response(schedule_serializers.data, status=status.HTTP_202_ACCEPTED)
            else:
                return Response(schedule_serializers.errors, status=status.HTTP_400_BAD_REQUEST)
        # delete
        elif request.method == 'DELETE':
            schedule.delete()
            return Response({'message':'Deleted'}, status=status.HTTP_202_ACCEPTED)
    
    else:
        return Response({'message':"Don't found"}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def bus_route_api_view(request):

    # list
    if request.method == 'GET':
        bus_routes = models.BusRoute.objects.all()
        bus_routes_serializers = serializers.BusRouteSerializers(bus_routes, many=True)
        return Response(bus_routes_serializers.data, status=status.HTTP_200_OK)

    # create
    elif request.method == 'POST':
        bus_route_serializers = serializers.BusRouteSerializers(data=request.data)
        # validation
        if bus_route_serializers.is_valid():
            bus_route_serializers.save()
            return Response({'message':'Created'}, status=status.HTTP_201_CREATED)
        else:
            return Response(bus_route_serializers.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def bus_route_detail_view(request, pk: int=None):

    # queryset
    bus_route = models.BusRoute.objects.filter(pk=pk).first()

    # validation
    if bus_route:
        
        # retrieve
        if request.method == 'GET':
            bus_route_serializers = serializers.BusRouteSerializers(bus_route)
            return Response(bus_route_serializers.data, status=status.HTTP_200_OK)
        # update
        elif request.method == 'PUT':
            bus_route_serializers = serializers.BusRouteSerializers(bus_route, data=request.data)
            if bus_route_serializers.is_valid():
                bus_route_serializers.save()
                return Response(bus_route_serializers.data, status=status.HTTP_202_ACCEPTED)
            else:
                return Response(bus_route_serializers.errors, status=status.HTTP_400_BAD_REQUEST)
        # delete
        elif request.method == 'DELETE':
            bus_route.delete()
            return Response({'message':'Deleted'}, status=status.HTTP_202_ACCEPTED)
    
    else:
        return Response({'message':"Don't found"}, status=status.HTTP_400_BAD_REQUEST)