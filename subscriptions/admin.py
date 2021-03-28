from django.contrib import admin
from .models import Subscription, Category

# Register your models here.


class SubscriptionAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'rating',
        'discounts',
        'database_access',
        'forum_access',
        'email_support',
        'chat_support',
        'video_guides',
        'video_conferencing',
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
