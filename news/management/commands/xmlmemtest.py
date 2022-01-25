from django.core.management.base import BaseCommand
from myapp.helpers.scheduler import write_job_board_feed
import uuid

class Command(BaseCommand):
    def handle(self, *args, **options):
        write_job_board_feed("News", "", "just news fetch", nocache=uuid.uuid4())


# Run command :- ./manage.py xmlmemtest or python manage.py xmlmemtest