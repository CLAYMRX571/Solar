from modeltranslation.translator import register, TranslationOptions
from .models import Jobs, Abs, Res, Look, Offer, Apply, Info, Foot

@register(Jobs)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'deadline', 'location',)

@register(Abs)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'desc',)

@register(Res)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'desc',)

@register(Look)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'desc',)

@register(Offer)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'desc',)

@register(Apply)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'desc',)

@register(Info)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'desc', 'mail',)

@register(Foot)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('desc', 'button',)