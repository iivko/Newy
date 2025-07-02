from django.core.management.base import BaseCommand
from app.models import New


news_data = [
    {
        "title": "Django 5.0 Released with Exciting Features",
        "author": "Alice Johnson",
        "facebook_link": "https://facebook.com/django-news-1",
        "twitter_link": "https://twitter.com/django-news-1",
        "linkedin_link": "https://linkedin.com/in/django-news-1",
        "content": "The Django community has announced version 5.0 with enhanced async support.",
        "status": "published",
    },
    {
        "title": "AI Generates News at Scale",
        "author": "Bob Smith",
        "facebook_link": "",
        "twitter_link": "",
        "linkedin_link": "",
        "content": "Machine learning models are now used to auto-write news content across industries.",
        "status": "inprogress",
    },
    {
        "title": "Cybersecurity in 2025",
        "author": "Carol White",
        "facebook_link": "https://facebook.com/cyber-2025",
        "twitter_link": "",
        "linkedin_link": "https://linkedin.com/in/cyber-2025",
        "content": "Experts warn about quantum threats and push for post-quantum cryptography.",
        "status": "draft",
    },
    {
        "title": "Python Named Top Language Again",
        "author": "David Lin",
        "facebook_link": "",
        "twitter_link": "https://twitter.com/python-top",
        "linkedin_link": "",
        "content": "Python continues to dominate StackOverflow and GitHub statistics.",
        "status": "published",
    },
    {
        "title": "Remote Work Trends in Tech",
        "author": "Evelyn King",
        "facebook_link": "",
        "twitter_link": "",
        "linkedin_link": "",
        "content": "Major tech firms adopt hybrid and remote-first policies in 2025.",
        "status": "published",
    },
    {
        "title": "Blockchain Beyond Crypto",
        "author": "Frank Zhang",
        "facebook_link": "https://facebook.com/blockchain-news",
        "twitter_link": "https://twitter.com/blockchain-news",
        "linkedin_link": "",
        "content": "Companies now use blockchain for logistics, voting, and identity verification.",
        "status": "inprogress",
    },
    {
        "title": "Frontend Framework Wars Continue",
        "author": "Grace Kim",
        "facebook_link": "",
        "twitter_link": "",
        "linkedin_link": "",
        "content": "React, Vue, and Svelte continue to evolve rapidly.",
        "status": "draft",
    },
    {
        "title": "Open Source in Government",
        "author": "Henry Patel",
        "facebook_link": "",
        "twitter_link": "https://twitter.com/open-gov",
        "linkedin_link": "https://linkedin.com/in/open-gov",
        "content": "Governments worldwide are adopting open source software to reduce costs.",
        "status": "published",
    },
    {
        "title": "Quantum Computing Breakthroughs",
        "author": "Isabel Gomez",
        "facebook_link": "",
        "twitter_link": "",
        "linkedin_link": "https://linkedin.com/in/quantum-news",
        "content": "New hardware from major players achieves unprecedented coherence times.",
        "status": "inprogress",
    },
    {
        "title": "Green Tech Startups on the Rise",
        "author": "Jason Lee",
        "facebook_link": "https://facebook.com/green-tech",
        "twitter_link": "https://twitter.com/green-tech",
        "linkedin_link": "",
        "content": "Environmental innovation fuels a new wave of investment in green startups.",
        "status": "published",
    },
]


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
                }
            )

        self.stdout.write(self.style.SUCCESS("✅ News data populated successfully."))
