from django.core.management.base import BaseCommand
from news.seeds import seed_news
from users.seeds import seed_users


class Command(BaseCommand):
    help = "This command init app's seeds"

    def handle(self, *args, **options):
        seed_news()
        seed_users()