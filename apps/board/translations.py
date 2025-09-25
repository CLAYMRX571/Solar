from modeltranslation.translator import register, TranslationOptions
from .models import Board

@register(Board)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'desc', 'board_desc',)