from django.contrib import admin
from django.db import models
from django_ckeditor_5.widgets import CKEditor5Widget
from modeltranslation.admin import TranslationAdmin
from .models import Young, Fol, Met, Pic

@admin.register(Young)
class YoungAdmin(TranslationAdmin):
    list_display = ['name',]

@admin.register(Fol)
class FolAdmin(TranslationAdmin):
    list_display = ['name', 'desc', 'link',]

    formfield_overrides = {
        models.TextField: {'widget': CKEditor5Widget(config_name='default')},
    }

@admin.register(Met)
class MetAdmin(TranslationAdmin):
    list_display = ['name', 'desc', 'button',]

    formfield_overrides = {
        models.TextField: {'widget': CKEditor5Widget(config_name='default')},
    }

@admin.register(Pic)
class PicAdmin(TranslationAdmin):
    list_display = ['name',]