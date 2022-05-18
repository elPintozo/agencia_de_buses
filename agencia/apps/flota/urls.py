from django.urls import path
from apps.flota import views as view_flota
from apps.flota.api import apis as apis_flota

app_name='garage'

urlpatterns = [
    # APIs
    path('api/chauffeur/list', apis_flota.chauffeur_api_view, name='api-chauffeur-list'),
    path('api/chauffeur/detail/<int:pk>/', apis_flota.chauffeur_detail_view, name='api-chauffeur-detail'),

    path('api/bus/list', apis_flota.bus_api_view, name='api-bus-list'),
    path('api/bus/detail/<int:pk>/', apis_flota.bus_detail_view, name='api-bus-detail'),

    path('api/route/list', apis_flota.route_api_view, name='api-route-list'),
    path('api/route/detail/<int:pk>/', apis_flota.route_detail_view, name='api-route-detail'),
    path('api/route/assing_bus/<int:pk>/', apis_flota.assing_bus, name='api-route-assing-bus'),
    path('api/route/get_assinged_buses/<int:pk>/', apis_flota.get_assinged_buses, name='api-route-get-assinged-buses'),
    path('api/route/unassing_bus/<int:pk>/', apis_flota.unassing_bus, name='api-route-unassing-bus'),
    path('api/route/add/bus/', apis_flota.route_add_bus, name='api-route-add-bus'),
    path('api/route/remove/bus/', apis_flota.route_remove_bus, name='api-route-remove-bus'),

    path('api/schedule/list', apis_flota.schedule_api_view, name='api-schedule-list'),
    path('api/schedule/detail/<int:pk>/', apis_flota.schedule_detail_view, name='api-schedule-detail'),

    path('api/bus_route/list', apis_flota.bus_route_api_view, name='api-bus_route-list'),
    path('api/bus_route/detail/<int:pk>/', apis_flota.bus_route_detail_view, name='api-bus_route-detail'),

    # VIEWs
    path('bus/list/', view_flota.bus_list, name='bus-list'),
    path('chauffeur/list/', view_flota.chauffeur_list, name='chauffeur-list'),
    path('route/list/', view_flota.route_list, name='route-list'),
    path('schedule/list/', view_flota.schedule_list, name='schedule-list'),
]