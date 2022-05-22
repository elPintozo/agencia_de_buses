from django.shortcuts import render

# Create your views here.
def ticket_buy(request):
    """Buy ticket page"""

    data = {
        'title': 'Buy Ticket ',
        'nav_item':'ticket',
    }

    return render(request, 'boleteria/buy_ticket.html', data)

def statistics(request):
    """statistics page"""

    data = {
        'title': 'Check statistics',
        'nav_item':'statistics',
    }

    return render(request, 'boleteria/statistics.html', data)