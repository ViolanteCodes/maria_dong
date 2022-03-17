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

class HeroButton(models.Model):
    """Button for the landing page Hero"""
    hero = models.ForeignKey(Hero, on_delete=models.CASCADE, related_name='hero_buttons')
    button_text = models.CharField(max_length=255)
    button_link = models.URLField()
