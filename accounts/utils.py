import random

from django.utils import timezone


random.seed(timezone.now())


def create_new_staff_number():
    return str(random.randint(1000000000, 9999999999))
