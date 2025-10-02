from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import Award, Link

@admin.register(Award)
class AwardAdmin(TranslationAdmin):
    list_display = ['desc',]

@admin.register(Link)
class LinkAdmin(TranslationAdmin):
    list_display = ['name', 'awards', 'achieve', 'lead', 'fell', 'chall', 'jour',]
