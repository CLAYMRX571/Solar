from modeltranslation.translator import register, TranslationOptions
from .models import Incore
    
@register(Incore)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'desc', 'button_name', 'buttons_name', 'buttons_desc',)