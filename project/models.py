from django.db import models
from django.db.models.fields.related import OneToOneField


class Book(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    
    @classmethod 
    def multilangual_fields(cls):
        fields = ['name']
        return fields


class TextResource(models.Model):
    text    = models.OneToOneField("Text", verbose_name=("Text"), related_name='text_resource', on_delete=models.CASCADE, blank=True, null=True)
    mailto  = models.OneToOneField("Mailto", verbose_name=("Mailto"), related_name='text_resource', on_delete=models.CASCADE, blank=True, null=True)
    tel     = models.OneToOneField("Tel", verbose_name=("Tel"), related_name='text_resource', on_delete=models.CASCADE, blank=True, null=True)
    image   = models.OneToOneField("Image", verbose_name=("Image"), related_name='text_resource', on_delete=models.CASCADE, blank=True, null=True)
    map     = models.OneToOneField("Map", verbose_name=("Map"), related_name='text_resource', on_delete=models.CASCADE, blank=True, null=True)
    link    = models.OneToOneField("Link", verbose_name=("Link"), related_name='text_resource', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f'{self.text}' or f'{self.mailto}' or f'{self.tel}' or f'{self.image}' or f'{self.map}' or f'{self.link}'

class Text(models.Model):
    text = models.CharField(verbose_name="Text", max_length=10000, blank=True, null=True)

    def __str__(self):
        data = f'{self.text}'
        return data[:100]
    
    @classmethod 
    def multilangual_fields(cls):
        fields = ['text']
        return fields

class Mailto(models.Model):
    href = models.CharField(verbose_name="Href", max_length=512, blank=True, null=True)

    def __str__(self):
        data = f'{self.href}'
        return data[:100]

class Tel(models.Model):
    href = models.CharField(verbose_name="Href", max_length=512, blank=True, null=True)

    def __str__(self):
        data = f'{self.href}'
        return data[:100]

class Image(models.Model):
    href = models.CharField(verbose_name="Href", max_length=512, blank=True, null=True)

    def __str__(self):
        data = f'{self.href}'
        return data[:100]

class Map(models.Model):
    href = models.CharField(verbose_name="Href", max_length=512, blank=True, null=True)

    def __str__(self):
        data = f'{self.href}'
        return data[:100]

class Link(models.Model):
    href = models.CharField(verbose_name="Href", max_length=512, blank=True, null=True)

    def __str__(self):
        data = f'{self.href}'
        return data[:100]