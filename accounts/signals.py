from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import Group

from .models import LibrarianModel


# Create signal for assigning staff to user
# and add librarian group to user for
@receiver(post_save, sender=LibrarianModel)
def set_librarian_group(sender, instance, created, **kwargs):
    if created:
        librarian = Group.objects.first()
        instance.user.is_staff = True
        instance.user.save()
        instance.user.groups.add(librarian)

