from django.db import models

# Create your models here.

# https://django-location-field.readthedocs.io/en/latest/tutorials.html

# Create your models here.

class Sales(models.Model):
    country = models.CharField(max_length=55)
    sales = models.FloatField()
    value = models.FloatField()
    bounce = models.FloatField(max_length=100)
        
    def __str__(self):
        return str(self.country)

class Categories(models.Model):
    country = models.CharField(max_length=55)
    sales = models.FloatField()
    value = models.FloatField()

    
    def __str__(self):
        return str(self.country)
    
class Table(models.Model):
    author = models.CharField(max_length=55)
    functione = models.CharField(max_length=35)
    status = models.CharField(max_length=6)
    employed = models.DateTimeField()

    
    def __str__(self):
        return str(self.author)
    
class Virtual(models.Model):
    sound = models.FileField()
    artist = models.CharField(max_length=25)
    title = models.CharField(max_length=25)

    def __str__(self):
        return str(self.sound)
