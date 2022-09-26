from django.db import models
from datetime import date



class Person(models.Model):
    first_name = models.CharField(max_length = 69)
    middle_name = models.CharField(max_length = 69, blank=True, null=True)
    last_name = models.CharField(max_length = 69)
    description = models.TextField()
    email = models.EmailField(max_length = 254)  # 254 is standard maximum string length

    # https://www.geeksforgeeks.org/datetimefield-django-forms/#:~:text=DateTimeField%20in%20Django%20Forms%20is,date%20and%20time%20from%20user.
    birthday = models.DateField()

    # roles = ...

    # location?
    # major?
    # minor?
    # achievements?

    def __str__(self):
        return self.full_name

    @property
    def full_name(self):
        return f"{self.first_name} {self.middle_name[0]} {self.last_name}"

    @property
    def age(self):
        # https://stackoverflow.com/a/9754466
        born = self.birthday
        today = date.today()
        return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

    def __str__(self):
        return self.full_name

class Entity(models.Model):
    name = models.CharField(max_length = 69)
    description = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        abstract = True

class Organization(Entity):
    pass

class Role(Entity):
    pass
