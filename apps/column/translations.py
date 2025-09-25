from modeltranslation.translator import register, TranslationOptions
from .models import Column

@register(Column)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'desc', 'board_desc',)