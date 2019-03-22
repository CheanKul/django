from django.db import models
from djongo import models

# Create your models here.


class Post(models.Model):
    Header = models.CharField(max_length=200)
    Content = models.TextField()
    ImageURL = models.TextField()

    def __str__(self):
        return self.Header


class User(models.Model):
    FirstName = models.CharField(max_length=200)
    LastName = models.CharField(max_length=200)
    Address = models.TextField()
    Posts = models.ManyToManyField(Post)

    def __str__(self):
        return self.FirstName+' '+self.LastName
