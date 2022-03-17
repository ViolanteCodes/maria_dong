from django.shortcuts import render
from django.views.generic.base import ContextMixin
from layout.models import NavBar

# Create your views here.

def landing_page(request):
    """View to return landing Page"""
    return render(request, 'landing_page.html', {})