from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from app.models import New
from .data import news_data



user = get_user_model()

class Command(BaseCommand):
    """
        Help command for populating the DB.
        Use only in DEBUG=True
    """

    help = "Populate the DB with dump data"


    def handle(self, *args, **options):
        for entry in news_data:
            obj, created = New.objects.get_or_create(
                title=entry["title"],
                defaults={
                    "author": entry["author"],
                    "facebook_link": entry["facebook_link"],
                    "twitter_link": entry["twitter_link"],
                    "linkedin_link": entry["linkedin_link"],
                    "content": entry["content"],
                    "status": entry["status"],
                    "creator": user.objects.get(id=1)
                }
            )

        self.stdout.write(self.style.SUCCESS("✅ News data populated successfully."))
