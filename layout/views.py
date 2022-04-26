from django.shortcuts import render
from django.http import Http404
from django.views.generic import TemplateView

# Import Butter
from django.conf import settings
from butter_cms import ButterCMS
Butter = ButterCMS(settings.BUTTER_TOKEN)

from datetime import datetime
# Import Pretty Printer
import pprint
pp = pprint.PrettyPrinter(indent=2)
# Create your views here.

class ButterPageView(TemplateView):
    """Base Butter Page View"""

    def get(self, request, page_slug=None, *args, **kwargs):
        context = self.get_context_data(page_slug, *args, **kwargs)
        return self.render_to_response(context)


    def get_context_data(self, page_slug=None, *args, **kwargs):
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
        if page_slug is not None:
            page_data = self.get_page(page_slug=page_slug, params=params)
            context['page_data'] = page_data
        if 'page_type' in self.kwargs:
            page_type = self.kwargs['page_type']
            page_type_data = self.get_page_type(page_type=page_type, params=params)
            context['page_type_data'] = page_type_data
        return context

    def get_menu(self):
        """Function to retrieve main navigation menu from butter"""
        params = {
        'page': '1',
        'page_size': '10'
        }
        nav_menu = Butter.content_fields.get(['navigation_menu'], params)
        return nav_menu['data']['navigation_menu'][0]['menu_items']

    def get_page(self, page_type='*', page_slug=None, params={}):
        """Fetch a page from butter"""
        if page_slug is not None:
            page_data = Butter.pages.get(page_type, page_slug, params)['data']['fields']
            # pp.pprint(page_data)
            return page_data

    def get_page_type(self, page_type='*', preview='0', params={}):
        """Fetch a page type from butter"""
        page_type_data = Butter.pages.all(page_type, params)['data']
        if page_type=='short':
            sorted_pieces = self.sort_pieces(pieces=page_type_data)
            pp.pprint(sorted_pieces)
            return sorted_pieces
        return page_type_data

    def sort_pieces(self, pieces=[]):
        """Sort page_type_data for shorts"""
        essay = []
        short_fiction = []
        poetry = []
        for piece in pieces:
            for field_key, field_value in piece['fields'].items():
                # Convert 'false' strings and empty lists to None for template
                if field_value == 'false' or not field_value:
                    piece['fields'][field_key] = None
                # convert isodate to python datetime object
                if field_key == 'publication_date':
                    pub_date = datetime.fromisoformat(field_value)
                    piece['fields']['publication_date'] = pub_date
            piece_type = piece['fields']['piece_type']
            if piece_type == 'short-fiction':
                short_fiction.append(piece['fields'])
            elif piece_type == 'poetry':
                poetry.append(piece['fields'])
            elif piece_type == 'essay':
                essay.append(piece['fields'])
            else:
                print('Piece type not found')
        self.new_shorts_dict = {
            'short_fiction': tuple(short_fiction),
            'poetry': tuple(poetry),
            'essay': tuple(essay),
        }
        return self.new_shorts_dict
