from modeltranslation.translator import register, TranslationOptions
from .models import Achievement, Recept, Past

@register(Achievement)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'desc',)

@register(Recept)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'desc',)

@register(Past)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'desc',)