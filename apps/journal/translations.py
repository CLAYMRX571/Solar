from modeltranslation.translator import register, TranslationOptions
from .models import Journal, Table, Detail, Text
    
@register(Journal)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)

@register(Table)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)

@register(Detail)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'desc',)

@register(Text)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'desc', 'list',)