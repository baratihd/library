from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class PublisherModel(models.Model):
    name = models.CharField(max_length=30)
    address = models.ForeignKey('index.AddressModel', on_delete=models.CASCADE)
    website = models.URLField()

    def __str__(self):
        return self.name


class AuthorModel(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    email = models.EmailField()

    def __str__(self):
        return u'%s %s' % (self.first_name, self.last_name)


class BookCategory(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class BookModel(models.Model):
    title = models.CharField(max_length=100)
    category = models.ManyToManyField('BookCategory')
    authors = models.ManyToManyField('AuthorModel')
    publisher = models.ForeignKey('PublisherModel', on_delete=models.CASCADE)
    publication_date = models.DateField()

    def __str__(self):
        return self.title

    @property
    def get_authors(self):
        authors = self.authors.values_list('last_name', flat=True)
        return ', '.join(authors)

    @property
    def get_categories(self):
        categories = self.authors.values_list('title', flat=True)
        return ', '.join(categories)


class BookCheckOutModel(models.Model):
    book = models.ForeignKey('BookModel', on_delete=models.CASCADE)
    user_checkout = models.ForeignKey(User, on_delete=models.CASCADE)
    librarian = models.ForeignKey('accounts.LibrarianModel', on_delete=models.CASCADE)
    check_out_datetime = models.DateTimeField(auto_now_add=True)
    return_datetime = models.DateTimeField()

    def __str__(self):
        return u'%s - %s' % (self.user_checkout.username, self.book.title)
