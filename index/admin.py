from django.contrib import admin

from .models import AddressModel


@admin.register(AddressModel)
class AddressModelAdmin(admin.ModelAdmin):
    list_display = (
        'city',
        'state_province',
        'country',
    )
    search_fields = (
        'city',
        'state_province',
        'country',
    )

