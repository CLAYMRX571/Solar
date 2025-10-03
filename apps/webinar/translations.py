from modeltranslation.translator import register, TranslationOptions
from .models import Webinar, Bros, Bobs, Next, Crd
    
@register(Webinar)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'desc',)

@register(Bros)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'desc', 'link',)

@register(Bobs)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'desc',)

@register(Next)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)

@register(Crd)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('title', 'desc', 'button',)