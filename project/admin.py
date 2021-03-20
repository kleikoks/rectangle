from django.contrib import admin
# Register your models here.
from .models import *
from django.forms import TextInput, Textarea

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    pass

@admin.register(TextResource)
class TextResourceAdmin(admin.ModelAdmin):
    pass

@admin.register(Text)
class TextAdmin(admin.ModelAdmin):
    pass

@admin.register(Mailto)
class MailtoAdmin(admin.ModelAdmin):
    pass

@admin.register(Tel)
class TelAdmin(admin.ModelAdmin):
    pass

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    pass

@admin.register(Map)
class MapAdmin(admin.ModelAdmin):
    pass

@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    pass