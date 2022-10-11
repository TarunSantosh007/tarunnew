from django.db import models

# Create your models here.


class UserDetails(models.Model):

    name = models.CharField(max_length=50)
    address = models.TextField()
    mobile = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return self.name

class Info(models.Model):
    name = models.CharField(max_length=200)
    address = models.TextField()
    data = models.JSONField(null = False)
