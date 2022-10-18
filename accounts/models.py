from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from .utils import create_new_staff_number
from .managers import UserManager


# Create default custom user, we change fields
class User(AbstractUser):

    objects = UserManager()

    class Meta:
        db_table = 'auth_user'
        verbose_name = _('user')
        verbose_name_plural = _('users')


# create librarian model for managing checkout books.
class LibrarianModel(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    staff_code = models.CharField(
        max_length=10, editable=False, unique=True, default=create_new_staff_number
    )
    address = models.ForeignKey('index.AddressModel', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username}'
