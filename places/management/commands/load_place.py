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
        place_desc = response.json()

        place, created = Place.objects.get_or_create(
            title=place_desc['title'],
            description_short=place_desc['description_short'],
            description_long=place_desc['description_long'],
            coordinate_lng=place_desc['coordinates']['lng'],
            coordinate_lat=place_desc['coordinates']['lat'],
        )

        for position, img_link in enumerate(place_desc['imgs']):
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