from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = "Commands for creating users Through superuser access"

    

    def handle(self, *args, **options):
        User.objects.all().delete()

        return "All Users are deleted Successfully"
        