from django.contrib import admin
from django.db import models
from django_ckeditor_5.widgets import CKEditor5Widget
from modeltranslation.admin import TranslationAdmin
from .models import Support, Miss, Invol

@admin.register(Support)
class SupportAdmin(TranslationAdmin):
    list_display = ['name', 'desc', 'title',]

    formfield_overrides = {
        models.TextField: {'widget': CKEditor5Widget(config_name='default')},
    }

@admin.register(Miss)
class MissAdmin(TranslationAdmin):
    list_display = ['name', 'desc',]

    formfield_overrides = {
        models.TextField: {'widget': CKEditor5Widget(config_name='default')},
    }

@admin.register(Invol)
class InvolAdmin(TranslationAdmin):
    list_display = ['name', 'desc', 'link',]

    formfield_overrides = {
        models.TextField: {'widget': CKEditor5Widget(config_name='default')},
    }