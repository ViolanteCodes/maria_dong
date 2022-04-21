from django.contrib import admin
from django.urls import path, include
from layout.views import ButterView


urlpatterns = [
    path('', ButterView.as_view(template_name="landing_page.html"),
        kwargs={'page_slug': 'landing-page'}),
    path('books/<page_slug>/', ButterView.as_view(template_name='book_detail.html'),
        name="book_page"),
    # path('books/<book_slug>/', views.book_detail_page, name="book_detail_page"),
    # path('admin/', admin.site.urls),
    path("__reload__/", include("django_browser_reload.urls")),
]