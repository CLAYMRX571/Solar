from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import About, Key

@admin.register(About)
class AboutAdmin(TranslationAdmin):
    list_display = ['name', 'desc',]

@admin.register(Key)
class KeyAdmin(TranslationAdmin):
    list_display = ['name', 'desc', 'title', 'ches',]
