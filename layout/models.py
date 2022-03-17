from django.db import models
from books.models import Book
from ckeditor.fields import RichTextField

# Create your models here.
class Hero(models.Model):
    """CMS interface for the hero section"""
    name = models.CharField(max_length=255)
    hero_title = models.CharField(max_length=255, blank=True, null=True)
    hero_image = models.CharField(max_length=255)
    hero_text = RichTextField(blank=True, null=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="hero_sections")

    def __str__(self):
        return self.name

class HeroButton(models.Model):
    """Button for the landing page Hero"""
    hero = models.ForeignKey(Hero, on_delete=models.CASCADE, related_name='hero_buttons')
    button_text = models.CharField(max_length=255)
    button_link = models.URLField()

    def __str__(self):
        return self.button_text

class NavBar(models.Model):
    """Top-level model for navbar, composed of NavBarMenuItems."""
    name = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name

class NavLink(models.Model):
    """Items for the MenuBar. Can be a link, submenu, or both."""
    nav_bar = models.ForeignKey(NavBar, on_delete=models.CASCADE, related_name='nav_links')
    display_text = models.CharField(max_length=255, null=True, blank=True)
    url = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.display_text

