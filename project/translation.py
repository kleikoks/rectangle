from modeltranslation.translator import translator, TranslationOptions
from django.apps import apps


for model in apps.get_models():
    if hasattr(model, 'multilangual_fields'):
        translator.register(model, fields=model.multilangual_fields())

# class BookTranslationOptions(TranslationOptions):
#     fields = ('name')
