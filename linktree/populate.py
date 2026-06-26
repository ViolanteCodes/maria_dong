# Import Butter
from django.conf import settings
from butter_cms import ButterCMS
Butter = ButterCMS(settings.BUTTER_TOKEN)
from linktree.models import Link

def populate_feature_links():
    feature_links = Butter.pages.get('links_page', 'link-tree')["data"]["fields"]["links"]
    for feature_link in feature_links:
        Link.objects.create(
            display_text = feature_link["display_text"],
            url = feature_link["url"]
        )
