from modeltranslation.translator import register, TranslationOptions
from .models import Webinar
    
@register(Webinar)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'desc', 'techno_desc',)