from django.core.management.base import BaseCommand

from archive.tasks import scrape_spinoffs


class Command(BaseCommand):
    def handle(self, *args, **options):
        scrape_spinoffs()
