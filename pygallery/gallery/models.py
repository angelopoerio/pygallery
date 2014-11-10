from django.db import models

# Create your models here.
class Picture(models.Model):
	image = models.ImageField(upload_to='static/images')
	notes = models.TextField(null=True, blank=True)
