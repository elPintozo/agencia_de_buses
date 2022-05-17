from django.shortcuts import render

def bus_list(request):
    """Bus list page"""

    data = {
        'title': 'Bus list',
        'nav_item':'bus',
    }

    return render(request, 'flota/bus_list.html', data)


def chauffeur_list(request):
    """Chauffeur list page"""

    data = {
        'title': 'Chauffeur list',
        'nav_item':'chauffeur',
    }

    return render(request, 'flota/chauffeur_list.html', data)

def route_list(request):
    """Route list page"""

    data = {
        'title': 'Route list',
        'nav_item':'route',
    }

    return render(request, 'flota/route_list.html', data)

def schedule_list(request):
    """Schedule list page"""

    data = {
        'title': 'Schedule list',
        'nav_item':'schedule',
    }

    return render(request, 'flota/schedule_list.html', data)