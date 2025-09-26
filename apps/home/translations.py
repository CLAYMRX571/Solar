from modeltranslation.translator import register, TranslationOptions
from .models import Banner, Home, Latest

@register(Banner)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)
    
@register(Home)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'desc', 'button_name', 'buttons_name', 'buttons_desc',)
    
@register(Latest)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('category_name', 'browse_link_name', 'latest_title', 'latest_desc',) 