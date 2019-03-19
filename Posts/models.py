from django.db import models
from djongo import models

# Create your models here.


class Post(models.Model):
    Header = models.CharField(max_length=200)
    Content = models.TextField()
    ImageURL = models.TextField()

    def __str__(self):
        return self.Header
