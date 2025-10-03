from django.contrib import admin
from django.db import models
from django_ckeditor_5.widgets import CKEditor5Widget
from modeltranslation.admin import TranslationAdmin
from .models import Advance

@admin.register(Advance)
class AdvanceAdmin(TranslationAdmin):
    list_display = ['name', 'desc', 'topic', 'performance',]

    formfield_overrides = {
        models.TextField: {'widget': CKEditor5Widget(config_name='default')},
    }