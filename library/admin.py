from django.contrib import admin

from .models import (
    PublisherModel,
    AuthorModel,
    BookCategory,
    BookModel,
)


@admin.register(PublisherModel)
class PublisherModelAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'website',
    )


@admin.register(AuthorModel)
class AuthorModelAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'last_name',
        'email',
    )


@admin.register(BookCategory)
class BookCategoryAdmin(admin.ModelAdmin):
    list_display = (
        'title',
    )


@admin.register(BookModel)
class BookModelAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'publisher',
        'publication_date',
    )
