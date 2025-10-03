from modeltranslation.translator import register, TranslationOptions
from .models import Column, Data, Mons

@register(Column)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'desc',)

@register(Data)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)

@register(Mons)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)