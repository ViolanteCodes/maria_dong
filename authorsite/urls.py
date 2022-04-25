from django.contrib import admin
from django.urls import path, include
from layout.views import ButterPageView


urlpatterns = [
    path('', ButterPageView.as_view(template_name="landing_page.html"),
        kwargs={'page_slug': 'landing-page'}),
    path('about/', ButterPageView.as_view(template_name="about.html"),
        kwargs={'page_slug': 'about'}, name="about"),
    path('books/', ButterPageView.as_view(template_name="books_list.html"), 
        kwargs={'page_slug': 'books'}, name="books_list"), 
    path('books/<page_slug>/', ButterPageView.as_view(template_name='book_detail.html'),
        name="book_page"),
    path('publications/', ButterPageView.as_view(template_name='shorts.html'), 
        kwargs={'page_slug':'publications', 'page_type':'short'}, name="publications"),
    path('admin/', admin.site.urls),
    path("__reload__/", include("django_browser_reload.urls")),
]