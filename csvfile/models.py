from django.db import models

# Create your models here.

class Mdata(models.Model):
    id = models.CharField(max_length=150, primary_key = True)
    name = models.CharField(max_length=500)
    date = models.CharField(max_length=50)
    location = models.CharField(max_length=150)
    def __str__(self):
        return self.name