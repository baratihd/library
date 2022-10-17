from django.views.generic import ListView

from .models import BookModel
from index.mixins import LoginRequiredMixin


class BookListView(LoginRequiredMixin, ListView):
    template_name = 'library/book_list.html'
    model = BookModel
    context_object_name = 'books'
    paginate_by = 10
