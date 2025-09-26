from modeltranslation.translator import register, TranslationOptions
from .models import Young
    
@register(Young)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'desc', 'techno_desc',)