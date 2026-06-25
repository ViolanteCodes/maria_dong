from django.shortcuts import render
from books.models import Book
from django.views.generic.detail import DetailView

# Create your views here.
# path('books/<page_slug>/', ButterPageView.as_view(template_name='book_detail.html'),
#     {'page_type': 'book', 'get_page_list': True}, name="book_page"),

class BookView(DetailView):
    model = Book
    template_name = "book_detail.html"
