from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=110)
    image = models.URLField(max_length=1000, default="https://www.hdwallpapers.in/walls/windows_xp_bliss-wide.jpg")
    link = models.URLField(max_length=250, default='https://github.com/TR-1000')

    def __str__(self):
        return self.title
        return self.description
        return self.technology
        return self.image
        return self.link
