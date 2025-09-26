from modeltranslation.translator import register, TranslationOptions
from .models import Daniel

@register(Daniel)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'desc', 'eco_desc',)