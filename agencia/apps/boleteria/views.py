from django.shortcuts import render

# Create your views here.
def ticket_list(request):
    """Ticket list page"""

    data = {
        'title': 'Ticket list',
        'nav_item':'ticket',
    }

    return render(request, 'boleteria/ticket_list.html', data)