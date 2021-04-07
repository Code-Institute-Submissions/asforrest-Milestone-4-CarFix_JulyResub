# The following code was adapted from an answer on Stack Overflow by user ryanshow.
# Source: https://stackoverflow.com/questions/6319093/do-math-using-django-template-filter

from django import template
register = template.Library()


@register.filter
def excluding_tax(value):
    return float(value) / 1.21


@register.filter
def excluding_tax2(value):
    return value - excluding_tax
