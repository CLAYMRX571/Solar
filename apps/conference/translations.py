from modeltranslation.translator import register, TranslationOptions
from .models import Conference

@register(Conference)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'desc', 'board_desc',)