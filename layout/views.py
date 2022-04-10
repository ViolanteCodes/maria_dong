from django.shortcuts import render

# Import Butter
from django.conf import settings
from butter_cms import ButterCMS
Butter = ButterCMS(settings.BUTTER_TOKEN)

# Import Pretty Printer
import pprint
pp = pprint.PrettyPrinter(indent=4)
# Create your views here.

def get_menu():
    """Function to retrieve main navigation menu from butter"""
    params = {
    'page': '1',
    'page_size': '10'
    }
    nav_menu = Butter.content_fields.get(['navigation_menu'], params)
    return nav_menu['data']['navigation_menu'][0]['menu_items']

def landing_page(request):
    """View to return landing Page"""
    nav_menu = get_menu()
    params = {
    'page': '1',
    'page_size': '10',
    'levels': '3',
    }
    data = Butter.pages.get('*', 'landing-page', params)['data']['fields']
    return render(request, 'landing_page.html', {
        'data': data,
        'nav_menu': nav_menu
    })