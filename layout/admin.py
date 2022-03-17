from django.contrib import admin
from .models import Hero, HeroButton, NavBar, NavLink

class HeroButtonInline(admin.TabularInline):
    model = HeroButton
    extra = 0

class HeroAdmin(admin.ModelAdmin):
    model=Hero
    inlines=[HeroButtonInline, ]

class NavLinkInline(admin.TabularInline):
    model = NavLink
    extra = 0

class NavBarAdmin(admin.ModelAdmin):
    model = NavBar
    inlines = [NavLinkInline, ]

admin.site.register(Hero, HeroAdmin)
admin.site.register(HeroButton)
admin.site.register(NavBar, NavBarAdmin)
admin.site.register(NavLink)