from django.core.management.base import BaseCommand

from mysite.rssbot.feeds import update_feeds

class Command(BaseCommand):
    def handle(self, *args, **options):
        update_feeds()
