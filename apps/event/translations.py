from modeltranslation.translator import register, TranslationOptions
from .models import Event, Text, Greeb

@register(Event)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'desc', 'area', 'part', 'contact',)

@register(Text)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)

@register(Greeb)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'desc', 'button',)