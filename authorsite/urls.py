from django.contrib import admin
from django.urls import path, include
from layout.views import ButterView


urlpatterns = [
    path('', ButterView.as_view()),
    # path('books/<book_slug>/', views.book_detail_page, name="book_detail_page"),
    # path('admin/', admin.site.urls),
    path("__reload__/", include("django_browser_reload.urls")),
]