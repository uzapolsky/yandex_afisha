from django.http import response
from django.shortcuts import render, get_object_or_404
from django.http.response import JsonResponse
from .models import Place, Image

def get_place(request, place_id):
    place = get_object_or_404(Place, id=place_id)
    images = place.images.all().order_by('position')
    response = {
        'title': place.title,
        'imgs': [image.img.url for image in images],
        'description_short': place.description_short,
        'description_long': place.description_long,
        'coordinates':{
            'lng': place.coordinate_lng,
            'lat': place.coordinate_lat,
        },
    }
    return JsonResponse(response, json_dumps_params={'ensure_ascii': False, 'indent': 4})
