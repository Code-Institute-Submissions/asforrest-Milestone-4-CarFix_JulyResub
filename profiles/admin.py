from django.contrib import admin
from .models import UserProfile

# Register your models here.


class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        'default_phone_number',
        'default_street_address1',
        'default_street_address2',
        'default_town_or_city',
        'default_county',
        'default_postcode',
        'default_country',
        'total_credits',
        'car_fix_basic',
        'car_fix_pro',
    )


admin.site.register(UserProfile, ProfileAdmin)
