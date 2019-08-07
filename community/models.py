from django.db import models

# Create your models here.
class Article(models.Model):
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    contents = models.TextField()
    url = models.URLField()
    email = models.EmailField()
    cdate = models.DateTimeField(auto_now_add=True)

class Patient(models.Model):
    age = models.CharField(max_length=20)
    # gender1 = models.BooleanField()
    # gender2 = models.BooleanField()
    gender1 = models.CharField(max_length=5)
    gender2 = models.CharField(max_length=5)
    height = models.CharField(max_length=10)
    weight = models.CharField(max_length=10)
    waist = models.CharField(max_length=10)
    # disease1 = models.BooleanField()
    # disease2 = models.BooleanField()
    # disease3 = models.BooleanField()
    # smoking1 = models.BooleanField()
    # drinking1 = models.BooleanField()
    disease1 = models.CharField(max_length=5)
    disease2 = models.CharField(max_length=5)
    disease3 = models.CharField(max_length=5)
    smoking1 = models.CharField(max_length=5)
    drinking1 = models.CharField(max_length=5)