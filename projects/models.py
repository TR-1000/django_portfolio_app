from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=110)
    image = models.FilePathField(path="/img")
    link = models.URLField(max_length=250, default='https://github.com/TR-1000')
