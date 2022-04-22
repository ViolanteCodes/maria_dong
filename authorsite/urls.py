from django.contrib import admin
from django.urls import path, include
from layout.views import ButterPageView, ButterListView


urlpatterns = [
    path('', ButterPageView.as_view(template_name="landing_page.html"),
        kwargs={'page_slug': 'landing-page'}),
    path('books/', ButterListView.as_view(template_name="books_list.html"), 
        kwargs={'page_type': 'book'}, name="books_list"), 
    path('books/<page_slug>/', ButterPageView.as_view(template_name='book_detail.html'),
        name="book_page"),
    # path('books/<book_slug>/', views.book_detail_page, name="book_detail_page"),
    # path('admin/', admin.site.urls),
    path("__reload__/", include("django_browser_reload.urls")),
]