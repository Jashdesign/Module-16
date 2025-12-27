from django.urls import path
from .views import doctor_map

urlpatterns = [
    path("map/", doctor_map, name="doctor_map"),
]