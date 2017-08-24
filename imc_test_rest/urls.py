from django.conf.urls import url, include
from .views import *


urlpatterns = [
    url(r'^animal/(?P<animal_id>\d+)', get_animal, name='get_animal'),
    url(r'^area/(?P<area_id>\d+)', get_area, name='get_area'),
]