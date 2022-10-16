from django.db import models


class PublisherModel(models.Model):
    name = models.CharField(max_length=30)
    address = models.ForeignKey('index.AddressModel', on_delete=models.CASCADE)
    website = models.URLField()

    def __unicode__(self):
        return self.name


class AuthorModel(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    email = models.EmailField()

    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)


class BookCategory(models.Model):
    title = models.CharField(max_length=50)


class BookModel(models.Model):
    title = models.CharField(max_length=100)
    category = models.ManyToManyField('BookCategory')
    authors = models.ManyToManyField('AuthorModel')
    publisher = models.ForeignKey('PublisherModel', on_delete=models.CASCADE)
    publication_date = models.DateField()

    def __unicode__(self):
        return self.title
