from django.contrib import admin
from books.models import Book
from books.models import FeatureLink
from books.models import PurchaseLink

# Register your models here.
admin.site.register(Book)
admin.site.register(FeatureLink)
admin.site.register(PurchaseLink)

