from pyexpat import model
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from .utils import create_new_staff_number
from .managers import UserManager


class User(AbstractUser):

    objects = UserManager()

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')


class LibrarianModel(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    staff_code = models.CharField(
        max_length=10, editable=False, unique=True, default=create_new_staff_number
    )
    address = models.ForeignKey('index.AddressModel', on_delete=models.CASCADE)
