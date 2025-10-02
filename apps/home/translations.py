from modeltranslation.translator import register, TranslationOptions
from .models import Banner, Home, Messages, Latest, Slide, Slides

@register(Banner)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)
    
@register(Home)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'desc', 'button_name', 'buttons_name', 'buttons_desc',)

@register(Messages)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'title', 'desc', 'button',)

@register(Latest)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'title', 'desc', 'button',) 

@register(Slide)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)
    
@register(Slides)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)
    