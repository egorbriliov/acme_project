from django.contrib import admin

from .models import Birthday


@admin.register(Birthday)
class BirthdayAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'last_name',
        'birthday',
        'image'
        )
    list_editable = (
        'last_name',
        'birthday',
        'image'
    )
    search_fields = (
        'first_name',
        'last_name'
    )
    list_filter = (
        'birthday',
    )
    list_display_links = (
        'first_name',
    )
