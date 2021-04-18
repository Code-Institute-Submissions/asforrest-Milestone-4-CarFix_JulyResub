from django.contrib import admin
from .models import Order, OrderLineItem

# Register your models here.

class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total', 'lineitem_credits',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = ('order_number', 'date', 'order_total',
                       'sales_tax', 'original_cart',
                       'stripe_pid', 'order_credits',)

    fields = ('order_number', 'user_profile', 'date', 'full_name',
              'email', 'phone_number', 'country', 'county',
              'postcode', 'town_or_city', 'street_address1',
              'street_address2', 'order_total',
              'sales_tax', 'order_credits', 'original_cart', 'stripe_pid',)

    list_display = ('order_number', 'date', 'full_name',
                    'order_total', 'order_credits',)

    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)