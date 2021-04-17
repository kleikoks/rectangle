from django.db import models


class Href(models.Model):
    href = models.CharField(verbose_name="Href", max_length=1024, blank=True, null=True)
    class Meta:
        abstract = True

class PageCode(models.Model):
    page_code = models.CharField(verbose_name="Href", max_length=512, blank=True, null=True)
    class Meta:
        abstract = True

class Text(PageCode):
    text = models.TextField(verbose_name="Text", blank=True, null=True)

    def __str__(self):
        data = f'{self.text}'
        return data[:100]
    
    @classmethod 
    def multilangual_fields(cls):
        fields = ['text']
        return fields

class Mailto(Href, PageCode):
    def __str__(self):
        data = f'{self.href}'
        return data[:100]

class Tel(Href, PageCode):
    def __str__(self):
        data = f'{self.href}'
        return data[:100]

class Image(Href, PageCode):
    def __str__(self):
        data = f'{self.href}'
        return data[:100]

class Map(Href, PageCode):
    def __str__(self):
        data = f'{self.href}'
        return data[:100]

class Link(Href, PageCode):
    def __str__(self):
        data = f'{self.href}'
        return data[:100]