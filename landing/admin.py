from django.contrib import admin

from .models import Hero, HeroButton

class HeroButtonInline(admin.TabularInline):
    model = HeroButton
    extra = 0

class HeroAdmin(admin.ModelAdmin):
    model=Hero
    inlines=[HeroButtonInline, ]

admin.site.register(Hero, HeroAdmin)
admin.site.register(HeroButton)