from django.db import models

# Create your models here.


class Brand(models.Model):

    class Meta:
        verbose_name_plural = 'Brands'

    name = models.CharField(max_length=254)
    # null=True and blank=True allows the field to be optional
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Mechanic(models.Model):
    # on_delete=models.SET_NULL allows a brand to be deleted 
    # without it deleting the mechanic
    brand = models.ForeignKey('Brand', null=True, blank=True, on_delete=models.SET_NULL)
    mechanic_name = models.CharField(max_length=254)
    primary_car_brand = models.CharField(max_length=254)
    biography = models.TextField(null=True, blank=True)
    year_joined = models.CharField(max_length=4, null=True, blank=True)
    rating = models.DecimalField(max_digits=5, decimal_places=1, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.mechanic_name
