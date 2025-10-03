from modeltranslation.translator import register, TranslationOptions
from .models import Incore, Core, Tess
    
@register(Incore)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)

@register(Core)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'desc', 'core_name', 'core_desc',)

@register(Tess)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'desc',)