from django.db import models

class Book(models.Model):
    name    = models.CharField(verbose_name="Назва книги",max_length=250, blank=True, null=True)
    type    = models.CharField(verbose_name="Назва книги",max_length=250, blank=True, null=True)
    line    = models.CharField(verbose_name="Назва книги",max_length=250, blank=True, null=True)

