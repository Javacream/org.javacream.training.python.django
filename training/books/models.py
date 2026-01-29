from django.db import models

from django.db import models

class Publisher(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self) -> str:
        return self.name


class Author(models.Model):
    lastname = models.CharField(max_length=100)
    firstname = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f"{self.firstname} {self.lastname}"


class Book(models.Model):
    isbn = models.CharField(max_length=13, primary_key=True)
    title = models.CharField(max_length=255)
    pages = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2)

    publisher = models.ForeignKey(Publisher, on_delete=models.PROTECT, related_name="books")
    authors = models.ManyToManyField(Author, related_name="books")

    def __str__(self) -> str:
        return f"{self.title} ({self.isbn})"
