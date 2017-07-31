from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.TextField(max_length=400, default='0')

    def __str__(self):
        return 'Kategoria ' + ' ' +  self.name


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    image = models.ImageField()
    category = models.ManyToManyField(Category, default='Brak Kategorii')
    incroduction = models.TextField(max_length=2000)
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title



class About(models.Model):
    introduction = models.TextField()
    text = models.TextField()
    image = models.ImageField()


