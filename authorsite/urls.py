from django.contrib import admin
from django.urls import path, include
from landing import views


urlpatterns = [
    path('', views.landing_page),
    path('admin/', admin.site.urls),
    path("__reload__/", include("django_browser_reload.urls")),
]