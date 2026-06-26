from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

    
class BookCover(models.Model):
    cover_image = models.ImageField(blank=True)
    alt_text = models.TextField(blank=True)
    name = models.CharField(blank=True)

    def __str__(self):
        return self.name
    
class Tag(models.Model):
    name = models.CharField()

    def __str__(self):
        return self.name

class Book(models.Model):
    """Book"""
    title = models.CharField(blank=True)
    slug = models.SlugField(blank=True)
    cover_image = models.ForeignKey('images.Image', on_delete=models.PROTECT, blank=True, null=True)
    short_description = models.TextField(blank=True)
    long_description = RichTextField(blank=True)
    publication_date = models.DateField(blank=True, null=True)
    publisher = models.CharField(blank=True)
    goodreads_link = models.URLField(blank=True)
    tags = models.ManyToManyField('books.Tag', blank=True)
    isbn = models.IntegerField(blank=True, null=True)
    seo_block = models.ForeignKey('seo.SEOBlock', blank=True, null=True, on_delete=models.PROTECT)
    ordering = ["-publication_date"]

    def __str__(self):
        return self.title

class FeatureLink(models.Model):
    """Link class for 'Featured In' coverage"""
    book = models.ForeignKey('books.Book', on_delete=models.CASCADE)
    venue = models.CharField()
    link = models.URLField()

    def __str__(self):
        return f"{self.book}: {self.venue}"
    
class PurchaseLink(models.Model):
    """Link class for purchases"""
    book = models.ForeignKey('books.Book', on_delete=models.CASCADE)
    retailer_display_text = models.CharField()
    url = models.URLField()

    def __str__(self):
        return f"{self.book}: {self.retailer_display_text}"

class Blurb(models.Model):
    book = models.ForeignKey('books.Book', on_delete=models.CASCADE)
    attribution_name = models.CharField()
    attribution_description = models.CharField(blank=True)
    attribution_book = models.CharField(blank=True)
    short_blurb = models.CharField(blank=True)
    long_blurb = models.CharField(blank=True)
    full_blurb = models.TextField(blank=True)
    link = models.URLField(blank=True)

    def __str__(self):
        return f"{self.book}: {self.attribution_name}"

class BookExtra(models.Model):
    book = models.ForeignKey('books.Book', on_delete=models.CASCADE)
    display_text = models.CharField()
    url = models.URLField()
    description = models.CharField()

    def __str__(self):
        return f"{self.book}: {self.display_text}"
    
