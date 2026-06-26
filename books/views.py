from books.models import Book
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from seo.mixins import SEOBlockMixin

class BookView(DetailView):
    model = Book
    template_name = "book_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["seo_block"] = self.object.seo_block
        return context

class BooksListView(SEOBlockMixin, ListView):
    model = Book
    template_name = "books_list.html"
    seo_block_slug = "books"
