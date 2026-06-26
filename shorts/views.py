from django.shortcuts import render
from seo.mixins import SEOBlockMixin
from shorts.models import Short
from django.views.generic.list import ListView

class ShortsListView(SEOBlockMixin, ListView):
    model = Short
    template_name = "shorts.html"
    seo_block_slug = "shorts"
