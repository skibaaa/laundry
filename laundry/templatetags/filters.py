from django import template

register = template.Library()

@register.filter(name="pair")
def pair(value, arg):
    return (value, arg)

@register.filter(name="get")
def get(value, key):
    return value.get(key)
