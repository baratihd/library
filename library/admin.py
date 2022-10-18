from django.contrib import admin

from .models import (
    PublisherModel,
    AuthorModel,
    BookCategory,
    BookModel,
    BookCheckOutModel,
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


@admin.register(BookCheckOutModel)
class BookCheckOutModelAdmin(admin.ModelAdmin):
    list_display = (
        'book',
        'user_checkout',
        'librarian',
        'check_out_datetime',
        'return_datetime',
    )
    search_fields = (
        'book__title',
        'book__publisher__first_name',
        'book__publisher__last_name',
        'user_checkout__user__first_name',
        'user_checkout__user__last_name',
    )
