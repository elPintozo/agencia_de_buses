from django.urls import path
from apps.flota.api import apis as apis_flota

app_name='garage'

urlpatterns = [
    path('api/chauffeur/list', apis_flota.chauffeur_api_view, name='api-chauffeur-list'),
    path('api/chauffeur/detail/<int:pk>/', apis_flota.chauffeur_detail_view, name='api-chauffeur-detail'),

    path('api/bus/list', apis_flota.bus_api_view, name='api-bus-list'),
    path('api/bus/detail/<int:pk>/', apis_flota.bus_detail_view, name='api-bus-detail'),

    path('api/route/list', apis_flota.route_api_view, name='api-route-list'),
    path('api/route/detail/<int:pk>/', apis_flota.route_detail_view, name='api-route-detail'),

    path('api/schedule/list', apis_flota.schedule_api_view, name='api-schedule-list'),
    path('api/schedule/detail/<int:pk>/', apis_flota.schedule_detail_view, name='api-schedule-detail'),

    path('api/bus_route/list', apis_flota.bus_route_api_view, name='api-bus_route-list'),
    path('api/bus_route/detail/<int:pk>/', apis_flota.bus_route_detail_view, name='api-bus_route-detail'),
]