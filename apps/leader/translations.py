from modeltranslation.translator import register, TranslationOptions
from .models import Leader

@register(Leader)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'more_name', 'desc', 'title', 'title_desc', 'file_name',)