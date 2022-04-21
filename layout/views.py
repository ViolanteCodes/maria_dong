from django.shortcuts import render
from django.http import Http404
from django.views.generic import TemplateView

# Import Butter
from django.conf import settings
from butter_cms import ButterCMS
Butter = ButterCMS(settings.BUTTER_TOKEN)

# Import Pretty Printer
import pprint
pp = pprint.PrettyPrinter(indent=4)
# Create your views here.

class ButterView(TemplateView):
    """Base Butter Page View"""

    def get(self, request, page_slug, *args, **kwargs):
        context = self.get_context_data(page_slug, *args, **kwargs)
        return self.render_to_response(context)


    def get_context_data(self, page_slug, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        # Get Menu
        if 'main_menu' not in self.kwargs or self.kwargs['main_menu'] != false:
            main_menu = self.get_menu()
            context['nav_menu'] = main_menu
        # Get Params or set default
        if 'params' in self.kwargs:
            params = self.kwargs['params']
        else:
            params = {
                'page': '1',
                'page_size': '10',
                'levels': '3',
            }
        # fetch page_data
        page_data = self.get_page(page_slug=page_slug, params=params)
        context['page_data'] = page_data
        return context

    def get_menu(self):
        """Function to retrieve main navigation menu from butter"""
        params = {
        'page': '1',
        'page_size': '10'
        }
        nav_menu = Butter.content_fields.get(['navigation_menu'], params)
        return nav_menu['data']['navigation_menu'][0]['menu_items']

    def get_page(self, page_type='*', page_slug="", params={}):
        """Fetch a page from butter"""
        page_data = Butter.pages.get(page_type, page_slug, params)['data']['fields']
        return page_data