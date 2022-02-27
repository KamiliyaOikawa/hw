from django.db import models

class Manga(models.Model):
    title = models.CharField(max_length= 150)
    image =models.ImageField(upload_to="media/")
