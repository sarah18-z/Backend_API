from django.db import models

# Create your models here.
class Category(models.Model):
    Category = models.CharField(max_length=200)

class Language(models.Model):
    language = models.CharField(max_length=200)

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=1000, default="")
    Category = models.ForeignKey(Category,on_delete=models.CASCADE)
    Language = models.ForeignKey(Language,on_delete=models.CASCADE)

