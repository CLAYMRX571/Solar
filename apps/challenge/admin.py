from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import Challenge, Anno, Wins

@admin.register(Challenge)
class ChallengeAdmin(TranslationAdmin):
    list_display = ['name', 'desc',]

@admin.register(Anno)
class AnnoAdmin(TranslationAdmin):
    list_display = ['desc',]

@admin.register(Wins)
class WinsAdmin(TranslationAdmin):
    list_display = ['name', 'desc', 'title',]