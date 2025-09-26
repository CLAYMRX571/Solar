from modeltranslation.translator import register, TranslationOptions
from .models import Structure

@register(Structure)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'desc',)