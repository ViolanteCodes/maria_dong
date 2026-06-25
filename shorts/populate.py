
from shorts.models import Short
from shorts.models import ReprintRecord
from shorts.models import ReviewRecord
from datetime import datetime

# Import Butter
from django.conf import settings
from butter_cms import ButterCMS
Butter = ButterCMS(settings.BUTTER_TOKEN)

def parse_publication_date(date_str):
    if not date_str:
        return None
    return datetime.fromisoformat(date_str.replace("Z", "")).date()

def populate_shorts():
    params = {'page_size': 50}
    shorts = Butter.pages.all(page_type="short", params=params)
    shorts = shorts["data"]
    for short in shorts:
        fields = short["fields"]
        short_record = Short.objects.create(
            piece_type = fields["piece_type"],
            title = fields["title"],
            piece_url = fields["piece_url"],
            published_in = fields["published_in"],
            issue = fields["issue"],
            publication_date = parse_publication_date(fields["publication_date"]),
            audio_available_url = fields["audio_available_url"],
            word_count = fields["word_count"],
            genre = fields["genre"]
        )
        if fields["reviewed_in"]:
            for entry in fields["reviewed_in"]:
                ReviewRecord.objects.create(
                    piece = short_record,
                    venue_name = entry["venue_name"],
                    venue_url = entry["venue_url"],
                    reviewed_date = parse_publication_date(entry["reviewed_date"])
                )
        if fields["reprinted_in"]:
            for entry in fields["reprinted_in"]:
                ReprintRecord.objects.create(
                    piece = short_record,
                    venue_name = entry["venue_name"],
                    venue_url = entry["vue_url"],
                    reprint_date = parse_publication_date(entry["reprint_date"])
                )
