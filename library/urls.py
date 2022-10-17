from django.urls import path

from .views import BookListView


app_name = 'library'
urlpatterns = [
    path('', BookListView.as_view(), name='book-list'),
]

