from modeltranslation.translator import register, TranslationOptions
from .models import Fellow

@register(Fellow)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'desc', 'focus_name', 'focus_desc',)