from django import template

from Django_Lesson import settings

register = template.Library()


@register.simple_tag
def media_path(value):
    if value:
        return f'/media/{value}'
    return '#'
