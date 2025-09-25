from modeltranslation.translator import register, TranslationOptions
from .models import Challenge

@register(Challenge)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'desc', 'board_desc') 