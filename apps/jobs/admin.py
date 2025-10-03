from django.contrib import admin
from django.db import models
from django_ckeditor_5.widgets import CKEditor5Widget
from modeltranslation.admin import TranslationAdmin
from .models import Jobs, Abs, Res, Look, Offer, Apply, Info, Foot

@admin.register(Jobs)
class JobsAdmin(TranslationAdmin):
    list_display = ['name', 'deadline', 'location',]

@admin.register(Abs)
class AbsAdmin(TranslationAdmin):
    list_display = ['name', 'desc',]

    formfield_overrides = {
        models.TextField: {'widget': CKEditor5Widget(config_name='default')},
    }

@admin.register(Res)
class ResAdmin(TranslationAdmin):
    list_display = ['name', 'desc',]

    formfield_overrides = {
        models.TextField: {'widget': CKEditor5Widget(config_name='default')},
    }

@admin.register(Look)
class LookAdmin(TranslationAdmin):
    list_display = ['name', 'desc',]

    formfield_overrides = {
        models.TextField: {'widget': CKEditor5Widget(config_name='default')},
    }

@admin.register(Offer)
class OfferAdmin(TranslationAdmin):
    list_display = ['name', 'desc',]

    formfield_overrides = {
        models.TextField: {'widget': CKEditor5Widget(config_name='default')},
    }

@admin.register(Apply)
class ApplyAdmin(TranslationAdmin):
    list_display = ['name', 'desc',]

    formfield_overrides = {
        models.TextField: {'widget': CKEditor5Widget(config_name='default')},
    }

@admin.register(Info)
class InfoAdmin(TranslationAdmin):
    list_display = ['name', 'desc', 'mail',]

    formfield_overrides = {
        models.TextField: {'widget': CKEditor5Widget(config_name='default')},
    }

@admin.register(Foot)
class FootAdmin(TranslationAdmin):
    list_display = ['desc', 'button',]

    formfield_overrides = {
        models.TextField: {'widget': CKEditor5Widget(config_name='default')},
    }
