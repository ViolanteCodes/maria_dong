
from books.models import Book
from books.models import FeatureLink

# Import Butter
from django.conf import settings
from butter_cms import ButterCMS
Butter = ButterCMS(settings.BUTTER_TOKEN)

def populate_feature_links(book:Book):
    feature_links = Butter.pages.get('book', book.slug)["data"]["fields"]["featured_in"]
    for feature_link in feature_links:
        FeatureLink.objects.create(
            book = book,
            venue = feature_link["venue"],
            link = feature_link["link"]
        )
