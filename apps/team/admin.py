from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import Team

@admin.register(Team)
class TeamAdmin(TranslationAdmin):
    list_display = ['name', 'desc', 'techno_desc',]
