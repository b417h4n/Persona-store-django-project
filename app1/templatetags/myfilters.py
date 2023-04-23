from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter(name='intspace')
@stringfilter
def intspace(value):
    orig = str(value)
    new = ""
    for i, char in enumerate(reversed(orig)):
        if i and (not (i % 3)):
            new += " "
        new += char
    return new[::-1]
