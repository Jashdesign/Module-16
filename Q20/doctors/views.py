from django.shortcuts import render
from django.conf import settings
from .models import Doctor

def doctor_map(request):
    doctors = Doctor.objects.values(
        "name",
        "specialization",
        "latitude",
        "longitude"
    )

    return render(request, "doctors/map.html", {
        "doctors": list(doctors),
        "google_maps_api_key": settings.GOOGLE_MAPS_API_KEY,
    })