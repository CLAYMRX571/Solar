from modeltranslation.translator import register, TranslationOptions
from .models import Structure, Column, Card

@register(Structure)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('desc',)

@register(Column)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('desc', 'button',)

@register(Card)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'desc', 'button',)