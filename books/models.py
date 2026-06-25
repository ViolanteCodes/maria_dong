from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

    

class Book(models.Model):
    """Book"""
    title = models.CharField(blank=True)
    slug = models.SlugField(blank=True)
    cover_image = models.ImageField(blank=True)
    alt_text = models.TextField(blank=True)
    short_description = models.TextField(blank=True)
    long_description = RichTextField(blank=True)
    publication_date = models.DateField(blank=True, null=True)
    publisher = models.CharField(blank=True)
    goodreads_link = models.URLField(blank=True)

    def __str__(self):
        return self.title

class FeatureLink(models.Model):
    """Link class for 'Featured In' coverage"""
    book = models.ForeignKey('books.Book', on_delete=models.CASCADE)
    venue = models.CharField()
    link = models.URLField()

    def __str__(self):
        return f"{self.book}: {self.venue}"

# class SEOFields(models.Model):
#     book = models.ForeignKey()
