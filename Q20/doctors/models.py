from django.db import models

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)

    location = models.CharField(max_length=150)
    experience = models.PositiveIntegerField(help_text="Years of experience")

    latitude = models.FloatField(default=20.5937)
    longitude = models.FloatField(default=78.9629)

    available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name