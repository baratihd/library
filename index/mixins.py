from django.contrib.auth.mixins import AccessMixin
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class LoginRequiredMixin(AccessMixin):
    """
    This mixin checking who can access the view.
    """
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

