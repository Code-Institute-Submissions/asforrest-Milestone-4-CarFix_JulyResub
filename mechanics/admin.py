from django.contrib import admin
from .models import Mechanic, Brand

# Register your models here.


class MechanicAdmin(admin.ModelAdmin):
    list_display = (
        'mechanic_name',
        'primary_car_brand',
        'rating',
        'biography',
        'year_joined',
        'image',
    )

    ordering = ('-rating',)


class BrandAdmin(admin.ModelAdmin):
    list_display = (
            'name',
            'friendly_name',
        )


admin.site.register(Mechanic, MechanicAdmin)
admin.site.register(Brand, BrandAdmin)
