from django.urls import path
from apps.flota import views as view_flota
from apps.flota.api import apis as apis_flota

app_name='garage'

urlpatterns = [
    # APIs
    path('api/chauffeur/list', apis_flota.chauffeur_api_view, name='api-chauffeur-list'),
    path('api/chauffeur/detail/<int:pk>/', apis_flota.chauffeur_detail_view, name='api-chauffeur-detail'),
    path('api/chauffeur/assing_route/<int:pk>/', apis_flota.chauffeur_assing_route, name='api-chauffeur-assing-route'),
    path('api/chauffeur/get_assinged_routes/<int:pk>/', apis_flota.chauffeur_get_assinged_routes, name='api-chauffeur-get-assinged-route'),
    path('api/chauffeur/unassing_route/<int:pk>/', apis_flota.chauffeur_unassing_route, name='api-chauffeur-unassing-route'),
    path('api/chauffeur/add/route/', apis_flota.chauffeur_add_route, name='api-chauffeur-add-route'),
    path('api/chauffeur/remove/route/', apis_flota.chauffeur_remove_route, name='api-chauffeur-remove-route'),

    path('api/bus/list', apis_flota.bus_api_view, name='api-bus-list'),
    path('api/bus/detail/<int:pk>/', apis_flota.bus_detail_view, name='api-bus-detail'),

    path('api/route/list', apis_flota.route_api_view, name='api-route-list'),
    path('api/route/detail/<int:pk>/', apis_flota.route_detail_view, name='api-route-detail'),
    path('api/route/assing_bus/<int:pk>/', apis_flota.route_assing_bus, name='api-route-assing-bus'),
    path('api/route/get_assinged_buses/<int:pk>/', apis_flota.route_get_assinged_buses, name='api-route-get-assinged-buses'),
    path('api/route/unassing_bus/<int:pk>/', apis_flota.route_unassing_bus, name='api-route-unassing-bus'),
    path('api/route/add/bus/', apis_flota.route_add_bus, name='api-route-add-bus'),
    path('api/route/remove/bus/', apis_flota.route_remove_bus, name='api-route-remove-bus'),

    path('api/schedule/list', apis_flota.schedule_api_view, name='api-schedule-list'),
    path('api/schedule/detail/<int:pk>/', apis_flota.schedule_detail_view, name='api-schedule-detail'),
    path('api/schedule/assing_route/<int:pk>/', apis_flota.schedule_assing_route, name='api-schedule-assing-route'),
    path('api/schedule/get_assinged_routes/<int:pk>/', apis_flota.schedule_get_assinged_routes, name='api-schedule-get-assinged-route'),
    path('api/schedule/unassing_route/<int:pk>/', apis_flota.schedule_unassing_route, name='api-schedule-unassing-route'),
    path('api/schedule/add/route/', apis_flota.schedule_add_route, name='api-schedule-add-route'),
    path('api/schedule/remove/route/', apis_flota.schedule_remove_route, name='api-schedule-remove-route'),

    path('api/bus_route/list', apis_flota.bus_route_api_view, name='api-bus_route-list'),
    path('api/bus_route/detail/<int:pk>/', apis_flota.bus_route_detail_view, name='api-bus_route-detail'),

    # VIEWs
    path('bus/list/', view_flota.bus_list, name='bus-list'),
    path('chauffeur/list/', view_flota.chauffeur_list, name='chauffeur-list'),
    path('route/list/', view_flota.route_list, name='route-list'),
    path('schedule/list/', view_flota.schedule_list, name='schedule-list'),
]