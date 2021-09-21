import requests
import uuid
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand
from places.models import Image, Place
from os.path import splitext


class Command(BaseCommand):
    help = 'Load place to website using .json description file'

    def add_arguments(self, parser):
        parser.add_argument('json-description', type=str)

    def handle(self, *args, **options):
        response = requests.get(options['json-description'])
        response.raise_for_status()
        raw_place = response.json()

        place, created = Place.objects.update_or_create(
            title=raw_place['title'],
            defaults={
                'description_short': raw_place['description_short'],
                'description_long': raw_place['description_long'],
                'coordinate_lng': raw_place['coordinates']['lng'],
                'coordinate_lat': raw_place['coordinates']['lat'],
            }
        )

        for position, img_link in enumerate(raw_place['imgs']):
            image, created = Image.objects.get_or_create(
                place=place,
                position=position,
            )
            _, img_ext = splitext(img_link)
            img = requests.get(img_link)
            response.raise_for_status()
            f = ContentFile(img.content)
            img_name = '{0}{1}'.format(str(uuid.uuid4()), img_ext)
            image.img.save(img_name, f, save=True)