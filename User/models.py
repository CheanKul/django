from django.db import models

# Create your models here.


class User(models.Model):
    FirstName = models.CharField(max_length=200)
    LastName = models.CharField(max_length=200)
    Username = models.CharField(max_length=200)
    Address = models.TextField()
    Email = models.CharField(max_length=100)

    def __str__(self):
        return self.FirstName+' '+self.LastName
