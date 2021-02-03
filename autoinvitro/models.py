from django.db import models

# Create your models here.

from django.db import models


# Create your models here.

class News(models.Model):
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=4000, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=50)
    visible = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Notification(models.Model):
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=4000, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=50)
    visible = models.BooleanField(default=False)


class Sale(models.Model):
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=4000, blank=True)
    cost = models.CharField(max_length=10)
    date = models.DateTimeField(auto_now_add=True)
    seller = models.CharField(max_length=50)
    visible = models.BooleanField(default=False)


class SaleItem(models.Model):
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=4000, blank=True)
    cost = models.CharField(max_length=10)
    seller = models.CharField(max_length=50)
    photo = models.CharField(max_length=300)
    visible = models.BooleanField(default=False)


class Car(models.Model):
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=4000, blank=True)
    date = models.DateTimeField(auto_now_add=False)
    mileage = models.CharField(max_length=7)
    cost = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    visible = models.BooleanField(default=False)


class Forum(models.Model):
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=4000, blank=True)
    numPosts = models.CharField(max_length=15)
    curator = models.CharField(max_length=7)


class Posts(models.Model):
    title = models.CharField(max_length=1, default='')
    forum = models.CharField(max_length=150)
    author = models.CharField(max_length=50)
    description = models.CharField(max_length=4000, blank=True)
    date = models.DateTimeField(auto_now_add=True)
