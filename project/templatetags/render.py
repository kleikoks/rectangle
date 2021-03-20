from django import template
from ..models import TextResource

register = template.Library()

@register.simple_tag
def render(id):
    obj = TextResource.objects.get(id=id)
    return obj


