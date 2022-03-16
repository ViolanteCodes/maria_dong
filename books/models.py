from django.db import models
from ckeditor.fields import RichTextField

class Book(models.Model):
    """Base Wagtail Page For A Book"""
    title = models.CharField(max_length=255)
    description = RichTextField(blank=True)
    goodreads_link = models.URLField(blank=True)

    def __str__(self):
        return self.title

class BuyLink(models.Model):
    """Buy Links for book"""
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='buy_links')
    retailer_name = models.CharField(max_length=255, blank=True)
    retailer_url = models.URLField(blank=True)

    def __str__(self):
        return self.retailer_name

class Blurb(models.Model):
    """Book Blurbs"""
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='blurbs')
    attribution_name = models.CharField(max_length=255, blank=True)
    attribution_description = RichTextField(blank=True)
    blurb_content = RichTextField(blank=True)

    def __str__(self):
        return self.attribution_name

class Territory(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'territories'

class Publisher(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name

class Edition(models.Model):
    """Specific Editions of Base Books"""

    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    media_type = models.CharField(max_length=255)
    on_sale_date = models.DateField(blank=True, null=True)
    flat_cover_image = models.CharField(max_length=255, blank=True, null=True)
    book_mockup = models.CharField(max_length=255, blank=True, null=True)
    territory = models.ForeignKey(Territory, on_delete=models.CASCADE)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)

    def __str__(self):
        return self.pk

