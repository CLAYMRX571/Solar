from modeltranslation.translator import register, TranslationOptions
from .models import Journal
    
@register(Journal)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'desc', 'long_desc',)