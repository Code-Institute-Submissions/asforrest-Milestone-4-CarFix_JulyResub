from django.db import models

# Create your models here.

class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'
    
    name = models.CharField(max_length=254)
    # null=True and blank=True allows the field to be optional
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Subscription(models.Model):
    # on_delete=models.SET_NULL allows a category to be deleted without it deleting the subscription
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    credits = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    video_conferencing = models.BooleanField(default=False)
    discounts = models.BooleanField(default=False, null=False, blank=False)
    forum_access = models.BooleanField(default=False)
    video_guides = models.BooleanField(default=False)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name