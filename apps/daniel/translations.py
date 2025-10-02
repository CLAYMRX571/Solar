from modeltranslation.translator import register, TranslationOptions
from .models import Daniel, Recep

@register(Daniel)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'desc', 'title',)

@register(Recep)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'desc',)