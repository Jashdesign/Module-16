from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'email',
        'age',
        'active',
        'created_at',
    )

    search_fields = (
        'name',
        'email',
    )

    list_filter = (
        'active',
        'created_at',
    )

    list_editable = (
        'active',
    )

    ordering = (
        'name',
    )

    readonly_fields = (
        'created_at',
    )

    fieldsets = (
        ("Student Info", {
            "fields": ("name", "email", "age")
        }),
        ("Status", {
            "fields": ("active",)
        }),
        ("System Info", {
            "fields": ("created_at",)
        }),
    )