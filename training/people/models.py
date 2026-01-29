from django.db import models

class Person(models.Model):
    lastname = models.CharField(max_length=100)
    firstname = models.CharField(max_length=100)
    height = models.PositiveSmallIntegerField(help_text="Height in cm")
    weight = models.FloatField(help_text="Weight in kg")               

    def __str__(self) -> str:
        return f"{self.firstname} {self.lastname}"

class Address(models.Model):
    street = models.CharField(max_length=200)
    city = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.street}, {self.city}"
