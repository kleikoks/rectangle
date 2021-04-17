from django.db import models
from django.db.models.expressions import OrderBy


class Book(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    price = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    order_num = models.PositiveIntegerField(default=0, blank=False, null=True)

    class Meta(object):
        ordering = ['order_num']
    
    @classmethod 
    def multilangual_fields(cls):
        fields = ['name']
        return fields


