from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from apps.boleteria import models
from apps.boleteria.api import serializers

@api_view(['GET', 'POST'])
def passenger_api_view(request):

    # list
    if request.method == 'GET':
        passengers = models.Passenger.objects.all()
        passengers_serializers = serializers.PassengerSerializers(passengers, many=True)
        return Response(passengers_serializers.data, status=status.HTTP_200_OK)

    # create
    elif request.method == 'POST':
        passengers_serializers = serializers.PassengerSerializers(data=request.data)
        # validation
        if passengers_serializers.is_valid():
            passengers_serializers.save()
            return Response({'message':'Created'}, status=status.HTTP_201_CREATED)
        else:
            return Response(passengers_serializers.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def passenger_detail_view(request, pk: int=None):

    # queryset
    passenger = models.Passenger.objects.filter(pk=pk).first()

    # validation
    if passenger:
        
        # retrieve
        if request.method == 'GET':
            passenger_serializers = serializers.PassengerSerializers(passenger)
            return Response(passenger_serializers.data, status=status.HTTP_200_OK)
        # update
        elif request.method == 'PUT':
            passenger_serializers = serializers.PassengerSerializers(passenger, data=request.data)
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
        tickets = models.Ticket.objects.all()
        tickets_serializers = serializers.TicketSerializers(tickets, many=True)
        return Response(tickets_serializers.data, status=status.HTTP_200_OK)

    # create
    elif request.method == 'POST':
        tickets_serializers = serializers.TicketSerializers(data=request.data)
        # validation
        if tickets_serializers.is_valid():
            tickets_serializers.save()
            return Response({'message':'Created'}, status=status.HTTP_201_CREATED)
        else:
            return Response(tickets_serializers.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def ticket_detail_view(request, pk: int=None):

    # queryset
    ticket = models.Ticket.objects.filter(pk=pk).first()

    # validation
    if ticket:
        
        # retrieve
        if request.method == 'GET':
            tickets_serializers = serializers.TicketSerializers(ticket)
            return Response(tickets_serializers.data, status=status.HTTP_200_OK)
        # update
        elif request.method == 'PUT':
            tickets_serializers = serializers.TicketSerializers(ticket, data=request.data)
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