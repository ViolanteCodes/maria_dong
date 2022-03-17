from django.shortcuts import render


# Create your views here.
def landing_page(request):
    """View to return landing Page"""
    return render(request, 'landing_page.html', {})