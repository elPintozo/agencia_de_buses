from django.shortcuts import render

# Create your views here.
def ticket_buy(request):
    """Buy ticket page"""

    data = {
        'title': 'Buy Ticket ',
        'nav_item':'ticket',
    }

    return render(request, 'boleteria/buy_ticket.html', data)