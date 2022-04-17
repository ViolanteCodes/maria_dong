from django.contrib import admin
from django.urls import path, include
from layout import views


urlpatterns = [
    path('', views.landing_page),
    path('books/<book_slug>/', views.book_page, name="book_page"),
    path('admin/', admin.site.urls),
    path("__reload__/", include("django_browser_reload.urls")),
]