from lib2to3.pytree import Base
from django.core.management.base import BaseCommand
from rooms.models import Amenity


class Command(BaseCommand):

    help = "This command creates amenities."

    """
    def add_arguments(self, parser):
        parser.add_argument(
            "--times", help="How many times do you want me to tell you I love you?"
        )
    """

    def handle(self, *args, **options):
        amenities = [
            "Air conditioning",
            "Alarm clock",
            "Balcony",
            "Wifi",
            "Internet",
            "Parking",
        ]

        for a in amenities:
            Amenity.objects.create(name=a)

        self.stdout.write(self.style.SUCCESS("Amenities created!"))
