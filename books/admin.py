from django.contrib import admin
from books.models import Book
from books.models import FeatureLink

# Register your models here.
admin.site.register(Book)
admin.site.register(FeatureLink)

