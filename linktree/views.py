from django.shortcuts import render
from django.views.generic import ListView
from seo.mixins import SEOBlockMixin
from linktree.models import Link

# Create your views here.

class LinkTreeView(SEOBlockMixin, ListView):
    seo_block_slug = "links"
    model = Link
    template_name = "links_page.html"
