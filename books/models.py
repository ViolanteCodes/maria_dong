from django.conf import settings
from django.db import models

# Create your models here.

    

class Book(models.Model):
    """Book"""
    title = models.CharField(blank=True)
    slug = models.SlugField(blank=True)
    cover_image = models.ImageField(blank=True)
    alt_text = models.TextField(blank=True)
    short_description = models.TextField(blank=True)
    long_description = models.TextField(blank=True)
    publication_date = models.DateField(blank=True, null=True)
    publisher = models.CharField(blank=True)
    goodreads_link = models.URLField(blank=True)

    def __str__(self):
        return self.title


# class SEOFields(models.Model):
#     book = models.ForeignKey()
