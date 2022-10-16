from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User


@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = (
        'username',
        'email',
        'first_name',
        'last_name',
        'last_login',
        'is_staff',
    )
    search_fields = (
        'username',
        'first_name',
        'last_name',
    )
