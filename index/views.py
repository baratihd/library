from django.views.generic import TemplateView


class HomeTemplateView(TemplateView):
    template_name = 'library/index.html'
