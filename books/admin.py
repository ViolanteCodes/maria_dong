from django.contrib import admin

from .models import Book, BuyLink, Blurb, Edition, Publisher, Territory

class BuyLinkInline(admin.TabularInline):
    model = BuyLink
    extra = 0

class BlurbInline(admin.StackedInline):
    model = Blurb
    extra = 0

class BookAdmin(admin.ModelAdmin):
    model=Book
    inlines=[BuyLinkInline, BlurbInline, ]

class EditionAdmin(admin.ModelAdmin):
    model=Edition

admin.site.register(Book, BookAdmin)
admin.site.register(Edition, EditionAdmin)
admin.site.register(Territory)
admin.site.register(Publisher)