from django.shortcuts import render
from places.models import Place, Image
from django.urls import reverse
from places.views import get_place

def index(request):
    places = Place.objects.all()
    places_geo = {
        'type': 'FeatureCollection',
        'features': []
    }
    for place in places:
        places_geo['features'].append(
            {
                'type': 'Feature',
                'geometry': 
                {
                    'type': 'Point',
                    'coordinates': [place.coordinate_lng, place.coordinate_lat]
                },
                'properties': 
                {
                    'title': place.title,
                    'placeId': place.id,
                    'detailsUrl': reverse(get_place, args=[place.id])
                }

            }
        )
    return render(request, 'index.html', context={'places_geo': places_geo})
    