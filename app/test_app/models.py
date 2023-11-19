from django.db import models


class AbstractAuthor(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    class Meta:
        abstract = True

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Library(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)


class Author(AbstractAuthor):
    pass


class Book(models.Model):
    title = models.CharField(max_length=100)
    year = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    library = models.ForeignKey(Library, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=8, decimal_places=2)


class LibraryBook(models.Model):
    library = models.ForeignKey(Library, on_delete=models.CASCADE)
    books = models.ManyToManyField(Book)