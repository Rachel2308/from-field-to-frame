from django.db import models

class Art(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    medium = models.CharField(max_length=100, null=True, blank=True)
    product_type = models.CharField(max_length=100, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.title