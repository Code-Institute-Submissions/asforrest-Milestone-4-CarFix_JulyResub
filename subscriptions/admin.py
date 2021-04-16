from django.contrib import admin
from .models import Subscription, Category

# Register your models here.


class SubscriptionAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'credits',
        'price',
        'video_conferencing',
        'discounts',
        'forum_access',
        'video_guides',
        'image',
    )

    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Subscription, SubscriptionAdmin)
admin.site.register(Category, CategoryAdmin)
