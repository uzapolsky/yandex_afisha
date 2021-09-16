from django.shortcuts import render
from places.models import Place, Image

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
                    'detailsUrl': '#'
                }

            }
        )
    return render(request, 'index.html', context={'places_geo': places_geo})
    