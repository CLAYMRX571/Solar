from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import Jobs, Abs, Res, Look, Offer, Apply, Info, Foot

@admin.register(Jobs)
class JobsAdmin(TranslationAdmin):
    list_display = ['name', 'deadline', 'location',]

@admin.register(Abs)
class AbsAdmin(TranslationAdmin):
    list_display = ['name', 'desc',]

@admin.register(Res)
class ResAdmin(TranslationAdmin):
    list_display = ['name', 'desc',]

@admin.register(Look)
class LookAdmin(TranslationAdmin):
    list_display = ['name', 'desc',]

@admin.register(Offer)
class OfferAdmin(TranslationAdmin):
    list_display = ['name', 'desc',]

@admin.register(Apply)
class ApplyAdmin(TranslationAdmin):
    list_display = ['name', 'desc',]

@admin.register(Info)
class InfoAdmin(TranslationAdmin):
    list_display = ['name', 'desc', 'mail',]

@admin.register(Foot)
class FootAdmin(TranslationAdmin):
    list_display = ['desc', 'button',]
