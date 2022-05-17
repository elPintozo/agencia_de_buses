from django.urls import path
from apps.boleteria import views as view_boleteria
from apps.boleteria.api import apis as apis_boleteria

app_name='box_office'

urlpatterns = [
    path('api/passenger/list', apis_boleteria.passenger_api_view, name='api-passenger-list'),
    path('api/passenger/detail/<int:pk>/', apis_boleteria.passenger_detail_view, name='api-passenger-detail'),

    path('api/ticket/list', apis_boleteria.ticket_api_view, name='api-ticket-list'),
    path('api/ticket/detail/<int:pk>/', apis_boleteria.ticket_detail_view, name='api-ticket-detail'),

    path('bus/list/', view_boleteria.ticket_list, name='ticket-list'),
]