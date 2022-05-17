from django.shortcuts import render

def home(request):
    """Principal page"""

    data = {
        'title': 'Home',
        'nav_item':'home',
    }

    return render(request, 'home.html', data)