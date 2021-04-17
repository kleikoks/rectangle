from django import template
from ..models import Text, Tel, Mailto, Link
from django.shortcuts import get_object_or_404

register = template.Library()

@register.simple_tag
def render(id, type='text'):
    if id and type == 'mailto':
        return get_object_or_404(Mailto, id=id)
    if id and type == 'tel':
        return get_object_or_404(Tel, id=id)
    if id and type == 'Link':
        return get_object_or_404(Link, id=id)
    return get_object_or_404(Text, id=id)


