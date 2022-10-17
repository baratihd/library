from django.db import models


class AddressModel(models.Model):
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=50)

    def __str__(self):
        return u'%s - %s' % (self.country, self.city)
