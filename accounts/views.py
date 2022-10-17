from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.views.generic.edit import CreateView

from .forms import UserCreationForm


class UserRegisterCreateView(SuccessMessageMixin, CreateView):
	template_name = 'accounts/register.html'
	form_class = UserCreationForm
	success_url = reverse_lazy('accounts:login')
	success_message = "Your profile was created successfully"


class UserLoginView(LoginView):
	template_name = 'accounts/login.html'

	def form_valid(self, form):
		user = form.get_user()
		messages.success(self.request, f'Welcome to library {user}')
		return super().form_valid(form)

