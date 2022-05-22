from django.urls import path
from apps.boleteria import views as view_boleteria
from apps.boleteria.api import apis as apis_boleteria

app_name='box_office'

urlpatterns = [
    path('api/passenger/list', apis_boleteria.passenger_api_view, name='api-passenger-list'),
    path('api/passenger/detail/<int:pk>/', apis_boleteria.passenger_detail_view, name='api-passenger-detail'),

    path('api/ticket/list', apis_boleteria.ticket_api_view, name='api-ticket-list'),
    path('api/ticket/detail/<int:pk>/', apis_boleteria.ticket_detail_view, name='api-ticket-detail'),
    
    path('api/ticket/list/buy', apis_boleteria.list_tickets_for_buy, name='api-ticket-list-buy'),
    path('api/ticket/list/sold', apis_boleteria.list_sold_tickets, name='api-ticket-list-sold'),
    path('api/ticket/pay', apis_boleteria.pay_ticket, name='api-ticket-pay'),

    path('ticket/buy', view_boleteria.ticket_buy, name='ticket-buy'),
    path('ticket/statistics', view_boleteria.statistics, name='statistics'),
    path('ticket/statistics/average', apis_boleteria.average_of_passengers, name='statistics-average'),
]