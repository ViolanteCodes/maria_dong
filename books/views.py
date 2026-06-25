from books.models import Book
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from seo.mixins import SEOBlockMixin

class BookView(DetailView):
    model = Book
    template_name = "book_detail.html"

class BooksListView(SEOBlockMixin, ListView):
    model = Book
    template_name = "books_list.html"
    seo_block_slug = "books"
