from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import Team, Cd

@admin.register(Team)
class TeamAdmin(TranslationAdmin):
    list_display = ['name', 'desc', 'button',]

@admin.register(Cd)
class CdAdmin(TranslationAdmin):
    list_display = ['name', 'title',]
