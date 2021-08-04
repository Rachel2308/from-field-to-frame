from django.db import models


class Furniture(models.Model):
    title = models.CharField(max_length=250, null=True, blank=True)
    product = models.CharField(max_length=250)
    medium = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField()
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.title
