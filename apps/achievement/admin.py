from django.contrib import admin
from django.db import models
from modeltranslation.admin import TranslationAdmin
from django_ckeditor_5.widgets import CKEditor5Widget
from .models import Achievement, Recept, Past

@admin.register(Achievement)
class AchievementAdmin(TranslationAdmin):
    list_display = ['name', 'desc',]

    formfield_overrides = {
        models.TextField: {'widget': CKEditor5Widget(config_name='default')},
    }

@admin.register(Recept)
class ReceptAdmin(TranslationAdmin):
    list_display = ['name', 'desc',]

    formfield_overrides = {
        models.TextField: {'widget': CKEditor5Widget(config_name='default')},
    }

@admin.register(Past)
class PastAdmin(TranslationAdmin):
    list_display = ['name', 'desc',]

    formfield_overrides = {
        models.TextField: {'widget': CKEditor5Widget(config_name='default')},
    }