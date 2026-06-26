from django.db import models

# Create your models here.

SHORT_TYPES = [
    ("short_fiction", "short fiction"),
    ("poetry", "poetry"),
    ("essay", "essay")
]

GENRES = [
    ("fantasy", "Fantasy"),
    ("science_fiction", "Science Fiction"),
    ("horror", "Horror")
]

class Short(models.Model):
    piece_type = models.CharField(choices=SHORT_TYPES)
    title = models.CharField()
    piece_url = models.URLField(blank=True)
    published_in = models.CharField(blank=True)
    issue = models.CharField(blank=True)
    publication_date = models.DateField(blank=True, null=True)
    audio_available_url = models.URLField(blank=True)
    word_count = models.CharField(blank=True)
    genre = models.CharField(choices=GENRES, blank=True)
    ordering = ["-publication_date"]

    def __str__(self):
        return self.title

class ReviewRecord(models.Model):
    piece = models.ForeignKey('shorts.Short', on_delete=models.CASCADE)
    venue_name = models.CharField()
    venue_url = models.URLField(blank=True)
    reviewed_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.piece} - {self.venue_name}"

class ReprintRecord(models.Model):
    piece = models.ForeignKey('shorts.Short', on_delete=models.CASCADE)
    venue_name = models.CharField()
    venue_url = models.URLField(blank=True)
    reprint_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.piece} -  {self.venue_name}"

