from django.db import models


# Create your models here.


class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30)
    county = models.CharField(max_length=30)
    website = models.URLField()

    def __str__(self):
        return self.name


class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):
        return self.first_namename


class Book(models.Model):
    title = models.CharField(max_length=30)
    author = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    Publication = models.DateField()

    def __str__(self):
        return self.title


