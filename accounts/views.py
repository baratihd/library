from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView

from .forms import UserCreationForm


class UserRegisterCreateView(SuccessMessageMixin, CreateView):
	template_name = 'accounts/register.html'
	form_class = UserCreationForm
	success_url = reverse_lazy('accounts:login')
	success_message = "Your profile was created successfully"
