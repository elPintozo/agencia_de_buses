import copy
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.db.models import Avg, Max, Min, Sum, Count

from apps.boleteria import models as models_boleteria
from apps.flota import models as models_flota
from apps.boleteria.api import serializers as serializers_boleteria
from apps.flota.api import serializers as serializers_flota

@api_view(['GET', 'POST'])
def passenger_api_view(request):

    # list
    if request.method == 'GET':
        passengers = models_boleteria.Passenger.objects.all()
        passengers_serializers = serializers_boleteria.PassengerSerializers(passengers, many=True)
        return Response(passengers_serializers.data, status=status.HTTP_200_OK)

    # create
    elif request.method == 'POST':
        passengers_serializers = serializers_boleteria.PassengerSerializers(data=request.data)
        # validation
        if passengers_serializers.is_valid():
            passengers_serializers.save()
            return Response({'message':'Created'}, status=status.HTTP_201_CREATED)
        else:
            return Response(passengers_serializers.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def passenger_detail_view(request, pk: int=None):

    # queryset
    passenger = models_boleteria.Passenger.objects.filter(pk=pk).first()

    # validation
    if passenger:
        
        # retrieve
        if request.method == 'GET':
            passenger_serializers = serializers_boleteria.PassengerSerializers(passenger)
            return Response(passenger_serializers.data, status=status.HTTP_200_OK)
        # update
        elif request.method == 'PUT':
            passenger_serializers = serializers_boleteria.PassengerSerializers(passenger, data=request.data)
            if passenger_serializers.is_valid():
                passenger_serializers.save()
                return Response(passenger_serializers.data, status=status.HTTP_202_ACCEPTED)
            else:
                return Response(passenger_serializers.errors, status=status.HTTP_400_BAD_REQUEST)
        # delete
        elif request.method == 'DELETE':
            passenger.delete()
            return Response({'message':'Deleted'}, status=status.HTTP_202_ACCEPTED)
    
    else:
        return Response({'message':"Don't found"}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def ticket_api_view(request):

    # list
    if request.method == 'GET':
        tickets = models_boleteria.Ticket.objects.all()
        tickets_serializers = serializers_boleteria.TicketSerializers(tickets, many=True)
        return Response(tickets_serializers.data, status=status.HTTP_200_OK)

    # create
    elif request.method == 'POST':
        tickets_serializers = serializers_boleteria.TicketSerializers(data=request.data)
        # validation
        if tickets_serializers.is_valid():
            tickets_serializers.save()
            return Response({'message':'Created'}, status=status.HTTP_201_CREATED)
        else:
            return Response(tickets_serializers.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def ticket_detail_view(request, pk: int=None):

    # queryset
    ticket = models_boleteria.Ticket.objects.filter(pk=pk).first()

    # validation
    if ticket:
        
        # retrieve
        if request.method == 'GET':
            tickets_serializers = serializers_boleteria.TicketSerializers(ticket)
            return Response(tickets_serializers.data, status=status.HTTP_200_OK)
        # update
        elif request.method == 'PUT':
            tickets_serializers = serializers_boleteria.TicketSerializers(ticket, data=request.data)
            if tickets_serializers.is_valid():
                tickets_serializers.save()
                return Response(tickets_serializers.data, status=status.HTTP_202_ACCEPTED)
            else:
                return Response(tickets_serializers.errors, status=status.HTTP_400_BAD_REQUEST)
        # delete
        elif request.method == 'DELETE':
            ticket.delete()
            return Response({'message':'Deleted'}, status=status.HTTP_202_ACCEPTED)
    
    else:
        return Response({'message':"Don't found"}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def list_tickets_for_buy(request):

    list_bus_route =  models_flota.BusRoute.objects.all()
    list_bus_route_serializers = serializers_flota.BusRouteSerializers(list_bus_route, many=True)
    return Response(list_bus_route_serializers.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def list_sold_tickets(request):

    list_ticket =  models_boleteria.Ticket.objects.all()
    list_ticket_serializers = serializers_boleteria.TicketSerializers(list_ticket, many=True)
    return Response(list_ticket_serializers.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def pay_ticket(request):
    
    # validate keys
    if 'dni_passenger' in request.data.keys() and 'seat_number' in request.data.keys() and 'bus_route' in request.data.keys():
        dni_passenger =  models_boleteria.Passenger.objects.filter(dni=request.data['dni_passenger']).first()
        
        # validate seat number
        if int(request.data['seat_number']) not in range(1,11):
            return Response({'message':"Don't seat number valid."}, status=status.HTTP_400_BAD_REQUEST)

        # Validate passenger
        if not dni_passenger:
            new_dni_passenger = models_boleteria.Passenger()
            new_dni_passenger.dni = request.data['dni_passenger']
            new_dni_passenger.save()
            dni_passenger = new_dni_passenger

        bus_route = models_flota.BusRoute.objects.filter(pk=request.data['bus_route']).first()

        if not bus_route:
            return Response({'message':"Don't route found"}, status=status.HTTP_400_BAD_REQUEST)
        
        ticket_selected = models_boleteria.Ticket.objects.filter(route=bus_route, seat_number=request.data['seat_number']).first()

        if not ticket_selected :
            new_ticket = models_boleteria.Ticket()
            new_ticket.passenger = dni_passenger
            new_ticket.route = bus_route
            new_ticket.seat_number = int(request.data['seat_number'])
            new_ticket.save()

            return Response({'message':'Paied ticket.'}, status=status.HTTP_200_OK)
        else:
            return Response({'message':"Don't sell this ticket, because saet number was used"}, status=status.HTTP_400_BAD_REQUEST)

    return Response({'message':"Don't found"}, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET'])
def average_of_passengers(request):

    # get data
    total = models_boleteria.Ticket.objects.aggregate(total=Count('id'))
    if total['total']:
        resume =  models_boleteria.Ticket.objects.values('route__route__name', 'route').annotate(count=Count('route'))
        
        # calculate data
        delta = 100/total['total']
        details = copy.deepcopy(resume)
        for p in details:
            p['average']= f"{p['count']*delta}%"
        
        return Response(details, status=status.HTTP_200_OK)

    return Response({'message':"Don't data found"}, status=status.HTTP_400_BAD_REQUEST)
