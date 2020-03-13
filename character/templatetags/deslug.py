from django import template

register = template.Library()

@register.filter
def deslug(value):
    return value.replace("-"," ")
