from django import template

register = template.Library()

@register.filter
def deslug(value):
    return value.replace("-"," ")

@register.simple_tag
def setvar(val=None):
    return val
