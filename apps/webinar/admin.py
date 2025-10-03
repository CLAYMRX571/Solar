from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import Webinar, Bros, Bobs, Next, Crd

@admin.register(Webinar)
class WebinarAdmin(TranslationAdmin):
    list_display = ['name', 'desc',]

@admin.register(Bros)
class BrosAdmin(TranslationAdmin):
    list_display = ['name', 'desc', 'link',]

@admin.register(Bobs)
class BobsAdmin(TranslationAdmin):
    list_display = ['name', 'desc',]

@admin.register(Next)
class NextAdmin(TranslationAdmin):
    list_display = ['name',]

@admin.register(Crd)
class CrdAdmin(TranslationAdmin):
    list_display = ['title', 'desc', 'button',]