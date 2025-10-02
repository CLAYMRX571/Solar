from modeltranslation.translator import register, TranslationOptions
from .models import Membership, Text, Board

@register(Membership)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'desc', 'column_name', 'column_desc', 'column_button',)

@register(Text)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('desc',)

@register(Board)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'desc', 'title', 'button',)