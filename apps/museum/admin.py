from django.contrib import admin
from django.db import models
from django_ckeditor_5.widgets import CKEditor5Widget
from modeltranslation.admin import TranslationAdmin
from .models import Museum, Ms, Mega, Supa

@admin.register(Museum)
class MuseumAdmin(TranslationAdmin):
    list_display = ['name',]

@admin.register(Ms)
class MsAdmin(TranslationAdmin):
    list_display = ['name', 'desc', 'button',]

    formfield_overrides = {
        models.TextField: {'widget': CKEditor5Widget(config_name='default')},
    }

@admin.register(Mega)
class MegaAdmin(TranslationAdmin):
    list_display = ['name',]

@admin.register(Supa)
class SupaAdmin(TranslationAdmin):
    list_display = ['name', 'desc', 'button',]

    formfield_overrides = {
        models.TextField: {'widget': CKEditor5Widget(config_name='default')},
    }
