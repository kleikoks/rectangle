from django.db import models

# Create your models here.
class WasteUtil(models.Model):
    name = models.CharField(max_length=150, blank=True, null=True)
    property = models.CharField(max_length=150, blank=True, null=True)
    category = models.ForeignKey(to='dj_rest_framework.WasteUtilCategory', on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return f'{self.name}'


class WasteUtilCategory(models.Model):
    name = models.CharField(max_length=150, blank=True, null=True)

    def __str__(self):
        return f'{self.name}'

class WasteUtilReview(models.Model):
    item = models.ForeignKey(to='dj_rest_framework.WasteUtil', on_delete=models.SET_NULL, blank=True, null=True, related_name='reviews')
    text = models.TextField(blank=True, null=True)
    viewed = models.BooleanField(blank=True, null=True, default=True)
