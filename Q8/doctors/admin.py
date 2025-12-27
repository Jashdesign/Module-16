from django.contrib import admin
from .models import Doctor

# Register your models here.
@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'specialization',
        'location',
        'experience',
        'available',
        'created_at'
    )
    list_filter = (
        'specialization',
        'location',
        'available',
    )

    search_fields = (
        'name',
        'specialization',
        'location',
    )

    list_editable = (
        'available',
    )

    ordering = (
        'name',
    )

    readonly_fields = (
        'created_at',
    )

    fieldsets = (
        ("Doctor Info", {
            "fields": ("name", "specialization", "experience")
        }),
        ("Location & Status", {
            "fields": ("location", "available")
        }),
        ("Metadata", {
            "fields": ("created_at",)
        }),
    )