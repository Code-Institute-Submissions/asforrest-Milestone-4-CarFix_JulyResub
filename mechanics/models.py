from django.db import models

# Create your models here.

class Specialty(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'
    
    name = models.CharField(max_length=254)
    # null=True and blank=True allows the field to be optional
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name

class Mechanic(models.Model):
    # on_delete=models.SET_NULL allows a specialty to be deleted without it deleting the product
    specialty = models.ForeignKey('Specialty', null=True, blank=True,
                                 on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    discounts = models.BooleanField(default=False, null=False, blank=False)
    database_access = models.BooleanField(default=False)
    forum_access = models.BooleanField(default=False)
    email_support = models.BooleanField(default=False)
    chat_support = models.BooleanField(default=False)
    video_guides = models.BooleanField(default=False)
    video_conferencing = models.BooleanField(default=False)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True,
                                 blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name