from django.contrib import admin
from django.db import models
from django_ckeditor_5.widgets import CKEditor5Widget
from modeltranslation.admin import TranslationAdmin
from .models import Team, Cd

@admin.register(Team)
class TeamAdmin(TranslationAdmin):
    list_display = ['name', 'desc', 'button',]

    formfield_overrides = {
        models.TextField: {'widget': CKEditor5Widget(config_name='default')},
    }

@admin.register(Cd)
class CdAdmin(TranslationAdmin):
    list_display = ['name', 'title',]
