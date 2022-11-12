from django.core.management.base import BaseCommand
from news.seeds import SeedNews


class Command(BaseCommand):
    help = "This command init app's seeds"

    def handle(self, *args, **options):
        SeedNews()
