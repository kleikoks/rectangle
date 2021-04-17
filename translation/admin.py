from django.contrib import admin
from .models import *

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