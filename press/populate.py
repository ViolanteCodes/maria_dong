from press.models import PressArticle
from layout.views import convert_date

# Import Butter
from django.conf import settings
from butter_cms import ButterCMS
Butter = ButterCMS(settings.BUTTER_TOKEN)

def populate_articles():
    params = {'page_size': 50}
    articles = Butter.content_fields.get(['interviews_and_articles'], params)
    for article in articles["data"]["interviews_and_articles"]:
            PressArticle.objects.create(
                title = article["title"],
                url = article["article_url"],
                publication_date = convert_date(article["publication_date"]),
                published_in = article["published_in"]
            )
