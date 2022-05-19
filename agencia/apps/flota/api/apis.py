from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from apps.flota import models
from apps.boleteria import models as models_boleteria
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

@api_view(['GET'])
def chauffeur_assing_route(request, pk: int=None):
    # queryset
    chauffeur = models.Chauffeur.objects.filter(pk=pk).first()

    # validation
    if chauffeur:
        exclude_route_list = models.BusRoute.objects.filter(chauffeur=chauffeur).values_list('route__name', flat=True)
        available_routes = models.Route.objects.exclude(name__in=exclude_route_list)
        available_routes_serializers = serializers.RouteSerializers(available_routes, many=True)
        return Response(available_routes_serializers.data, status=status.HTTP_200_OK)

    return Response({'message':"Don't chauffeur found"}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def chauffeur_get_assinged_routes(request, pk: int=None):
    # queryset
    chauffeur = models.Chauffeur.objects.filter(pk=pk).first()

    # validation
    if chauffeur:
        route_list = models.BusRoute.objects.filter(chauffeur=chauffeur).values_list('route__name', flat=True)
        assinged_routes = models.Route.objects.filter(name__in=route_list)
        assinged_routes_serializers = serializers.RouteSerializers(assinged_routes, many=True)
        return Response(assinged_routes_serializers.data, status=status.HTTP_200_OK)

    return Response({'message':"Don't chauffeur found"}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def chauffeur_unassing_route(request, pk: int=None):
    # queryset
    chauffeur = models.Chauffeur.objects.filter(pk=pk).first()

    # validation
    if chauffeur:
        buses_list = models.BusRoute.objects.filter(chauffeur=chauffeur).values_list('route__name', flat=True)
        assinged_routes = models.Route.objects.filter(name__in=buses_list)
        assinged_routes_serializers = serializers.RouteSerializers(assinged_routes, many=True)
        return Response(assinged_routes_serializers.data, status=status.HTTP_200_OK)

    return Response({'message':"Don't chauffeur found"}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def chauffeur_add_route(request):

    # validate keys
    if 'chauffeur' in request.data.keys() and 'selected_route' in request.data.keys():

        # get instances
        chauffeur = models.Chauffeur.objects.filter(pk=int(request.data['chauffeur'])).first()
        selected_route = models.Route.objects.filter(pk__in= request.data['selected_route'])

        # check if route has a assing chauffeur
        for route in selected_route:
            bus_route = models.BusRoute.objects.filter(chauffeur=chauffeur, route=route)
            if not bus_route:
                new_bus_route = models.BusRoute()
                new_bus_route.chauffeur = chauffeur
                new_bus_route.route = route
                new_bus_route.save()

        return Response({'message:':'Assinged'}, status=status.HTTP_200_OK)

    return Response({'message':"Don't chauffeur found"}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def chauffeur_remove_route(request):
    
    # validate keys
    if 'chauffeur' in request.data.keys() and 'selected_route' in request.data.keys():

        # get instances
        chauffeur = models.Chauffeur.objects.filter(pk=int(request.data['chauffeur'])).first()
        selected_route = models.Route.objects.filter(pk__in= request.data['selected_route'])

        # check if route has a assing bus
        for route in selected_route:
            bus_route = models.BusRoute.objects.filter(chauffeur=chauffeur, route=route)
            if bus_route:
                bus_route = bus_route.first()
                bus_route.chauffeur = None
                if bus_route.bus is None and bus_route.schedule is None:
                    bus_route.delete()
                else:
                    bus_route.save()

        return Response({'message:':'Assinged'}, status=status.HTTP_200_OK)

    return Response({'message':"Don't chauffeur found"}, status=status.HTTP_400_BAD_REQUEST)

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

@api_view(['GET'])
def route_assing_bus(request, pk: int=None):
    # queryset
    route = models.Route.objects.filter(pk=pk).first()

    # validation
    if route:
        exclude_buses_list = models.BusRoute.objects.filter(route=route).values_list('bus__plate', flat=True)
        available_buses = models.Bus.objects.exclude(plate__in=exclude_buses_list)
        available_buses_serializers = serializers.BusSerializers(available_buses, many=True)
        return Response(available_buses_serializers.data, status=status.HTTP_200_OK)

    return Response({'message':"Don't route found"}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def route_get_assinged_buses(request, pk: int=None):
    # queryset
    route = models.Route.objects.filter(pk=pk).first()

    # validation
    if route:
        buses_list = models.BusRoute.objects.filter(route=route).values_list('bus__plate', flat=True)
        assinged_buses = models.Bus.objects.filter(plate__in=buses_list)
        assinged_buses_serializers = serializers.BusSerializers(assinged_buses, many=True)
        return Response(assinged_buses_serializers.data, status=status.HTTP_200_OK)

    return Response({'message':"Don't route found"}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def route_unassing_bus(request, pk: int=None):
    # queryset
    route = models.Route.objects.filter(pk=pk).first()

    # validation
    if route:
        buses_list = models.BusRoute.objects.filter(route=route).values_list('bus__plate', flat=True)
        assinged_buses = models.Bus.objects.filter(plate__in=buses_list)
        assinged_buses_serializers = serializers.BusSerializers(assinged_buses, many=True)
        return Response(assinged_buses_serializers.data, status=status.HTTP_200_OK)

    return Response({'message':"Don't route found"}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def route_add_bus(request):

    # validate keys
    if 'route' in request.data.keys() and 'buses_selected' in request.data.keys():

        # get instances
        route = models.Route.objects.filter(pk=int(request.data['route'])).first()
        buses_selected = models.Bus.objects.filter(pk__in= request.data['buses_selected'])

        # check if route has a assing bus
        for bus in buses_selected:
            bus_route = models.BusRoute.objects.filter(route=route, bus=bus)
            if not bus_route:
                new_bus_route = models.BusRoute()
                new_bus_route.bus = bus
                new_bus_route.route = route
                new_bus_route.save()

        return Response({'message:':'Assinged'}, status=status.HTTP_200_OK)

    return Response({'message':"Don't route found"}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def route_remove_bus(request):
    
    # validate keys
    if 'route' in request.data.keys() and 'buses_selected' in request.data.keys():

        # get instances
        route = models.Route.objects.filter(pk=int(request.data['route'])).first()
        buses_selected = models.Bus.objects.filter(pk__in= request.data['buses_selected'])

        # check if route has a assing bus
        for bus in buses_selected:
            bus_route = models.BusRoute.objects.filter(route=route, bus=bus)
            if bus_route:
                bus_route = bus_route.first()
                bus_route.bus = None
                if bus_route.chauffeur is None and bus_route.schedule is None:
                    bus_route.delete()
                else:
                    bus_route.save()

        return Response({'message:':'Assinged'}, status=status.HTTP_200_OK)

    return Response({'message':"Don't route found"}, status=status.HTTP_400_BAD_REQUEST)

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

@api_view(['GET'])
def schedule_assing_route(request, pk: int=None):
    # queryset
    schedule = models.Schedule.objects.filter(pk=pk).first()

    # validation
    if schedule:
        exclude_route_list = models.BusRoute.objects.filter(schedule=schedule).values_list('route__name', flat=True)
        available_routes = models.Route.objects.exclude(name__in=exclude_route_list)
        available_routes_serializers = serializers.RouteSerializers(available_routes, many=True)
        return Response(available_routes_serializers.data, status=status.HTTP_200_OK)

    return Response({'message':"Don't schedule found"}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def schedule_get_assinged_routes(request, pk: int=None):
    # queryset
    schedule = models.Schedule.objects.filter(pk=pk).first()

    # validation
    if schedule:
        route_list = models.BusRoute.objects.filter(schedule=schedule).values_list('route__name', flat=True)
        assinged_routes = models.Route.objects.filter(name__in=route_list)
        assinged_routes_serializers = serializers.RouteSerializers(assinged_routes, many=True)
        return Response(assinged_routes_serializers.data, status=status.HTTP_200_OK)

    return Response({'message':"Don't schedule found"}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def schedule_unassing_route(request, pk: int=None):
    # queryset
    schedule = models.Schedule.objects.filter(pk=pk).first()

    # validation
    if schedule:
        buses_list = models.BusRoute.objects.filter(schedule=schedule).values_list('route__name', flat=True)
        assinged_routes = models.Route.objects.filter(name__in=buses_list)
        assinged_routes_serializers = serializers.RouteSerializers(assinged_routes, many=True)
        return Response(assinged_routes_serializers.data, status=status.HTTP_200_OK)

    return Response({'message':"Don't schedule found"}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def schedule_add_route(request):

    # validate keys
    if 'schedule' in request.data.keys() and 'selected_route' in request.data.keys():

        # get instances
        schedule = models.Schedule.objects.filter(pk=int(request.data['schedule'])).first()
        selected_route = models.Route.objects.filter(pk__in= request.data['selected_route'])

        # check if route has a assing schedule
        for route in selected_route:
            bus_route = models.BusRoute.objects.filter(schedule=schedule, route=route)
            if not bus_route:
                new_bus_route = models.BusRoute()
                new_bus_route.schedule = schedule
                new_bus_route.route = route
                new_bus_route.save()

        return Response({'message:':'Assinged'}, status=status.HTTP_200_OK)

    return Response({'message':"Don't schedule found"}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def schedule_remove_route(request):
    
    # validate keys
    if 'schedule' in request.data.keys() and 'selected_route' in request.data.keys():

        # get instances
        schedule = models.Schedule.objects.filter(pk=int(request.data['schedule'])).first()
        selected_route = models.Route.objects.filter(pk__in= request.data['selected_route'])

        # check if route has a assing bus
        for route in selected_route:
            bus_route = models.BusRoute.objects.filter(schedule=schedule, route=route)
            if bus_route:
                bus_route = bus_route.first()
                bus_route.schedule = None
                if bus_route.bus is None and bus_route.schedule is None:
                    bus_route.delete()
                else:
                    bus_route.save()

        return Response({'message:':'Assinged'}, status=status.HTTP_200_OK)

    return Response({'message':"Don't schedule found"}, status=status.HTTP_400_BAD_REQUEST)


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