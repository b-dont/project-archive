from django.db import models

class HomePage(models.Model):
    header = models.CharField(max_length=100, null=True)
    headshot = models.ImageField(blank=True, upload_to='home_images')
    bio = models.TextField(max_length=1000)
