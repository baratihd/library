from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from .utils import create_new_staff_number
from .managers import UserManager


class User(AbstractUser):

    objects = UserManager()

    class Meta:
        db_table = 'auth_user'
        verbose_name = _('user')
        verbose_name_plural = _('users')


class LibrarianModel(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    staff_code = models.CharField(
        max_length=10, editable=False, unique=True, default=create_new_staff_number
    )
    address = models.ForeignKey('index.AddressModel', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username}'

    def save(self, *args, **kwargs):
        is_created = not self.id
        if is_created:
            self.user.is_staff = True
            self.user.save()
        return super().save(args, kwargs)
