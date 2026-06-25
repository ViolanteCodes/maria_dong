
from books.models import Book
from books.models import FeatureLink
from books.models import Blurb

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

def populate_blurbs(book:Book):
    params = {'page_size': 50}
    blurbs = Butter.content_fields.get(['blurbs'], params)
    for blurb in blurbs["data"]["blurbs"]:
        if blurb["book"]["slug"] == book.slug:
            Blurb.objects.create(
                book = book,
                attribution_name = blurb["attribution_name"],
                attribution_description = blurb["attribution_description"] or "",
                attribution_book = blurb["attribution_book"] or "",
                short_blurb = blurb["short_blurb"] or "",
                long_blurb = blurb["long_blurb"] or "",
                full_blurb = blurb["full_blurb"] or "",
            )
