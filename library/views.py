from django.views.generic import ListView
from django.db.models import Q

from index.mixins import LoginRequiredMixin
from .models import BookModel
from .forms import BookSearchForm


class BookListView(ListView):
    template_name = 'library/book_list.html'
    model = BookModel
    context_object_name = 'books'
    paginate_by = None
    form = BookSearchForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.form
        return context

    def get_queryset(self):
        queryset = super().get_queryset().filter(
            Q(bookcheckoutmodel__isnull=True) |
            Q(bookcheckoutmodel__return_datetime__isnull=False)
        ).distinct()
        if 'search' in self.request.GET:
            self.form = self.form(self.request.GET)
            if self.form.is_valid():
                cd = self.form.cleaned_data['search']
                queryset = queryset.filter(
                    Q(title__icontains=cd) |
                    Q(category__title__icontains=cd) |
                    Q(authors__username__icontains=cd) |
                    Q(publisher__name__icontains=cd),
                )
        return queryset
