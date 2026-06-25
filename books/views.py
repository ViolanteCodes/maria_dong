from books.models import Book
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

class BookView(DetailView):
    model = Book
    template_name = "book_detail.html"

class BooksListView(ListView):
    model = Book
    template_name = "books_list.html"
