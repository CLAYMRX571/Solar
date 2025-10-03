from django.contrib import admin
from django.db import models
from modeltranslation.admin import TranslationAdmin
from django_ckeditor_5.widgets import CKEditor5Widget
from .models import About, Key

@admin.register(About)
class AboutAdmin(TranslationAdmin):
    list_display = ['name', 'desc',]

    formfield_overrides = {
        models.TextField: {'widget': CKEditor5Widget(config_name='default')},
    }

@admin.register(Key)
class KeyAdmin(TranslationAdmin):
    list_display = ['name', 'desc', 'title', 'ches',]

    formfield_overrides = {
        models.TextField: {'widget': CKEditor5Widget(config_name='default')},
    }
