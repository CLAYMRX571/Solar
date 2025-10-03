from django.contrib import admin
from django.db import models
from django_ckeditor_5.widgets import CKEditor5Widget
from modeltranslation.admin import TranslationAdmin
from .models import Webinar, Bros, Bobs, Next, Crd

@admin.register(Webinar)
class WebinarAdmin(TranslationAdmin):
    list_display = ['name', 'desc',]

    formfield_overrides = {
        models.TextField: {'widget': CKEditor5Widget(config_name='default')},
    }

@admin.register(Bros)
class BrosAdmin(TranslationAdmin):
    list_display = ['name', 'desc', 'link',]

    formfield_overrides = {
        models.TextField: {'widget': CKEditor5Widget(config_name='default')},
    }

@admin.register(Bobs)
class BobsAdmin(TranslationAdmin):
    list_display = ['name', 'desc',]

    formfield_overrides = {
        models.TextField: {'widget': CKEditor5Widget(config_name='default')},
    }

@admin.register(Next)
class NextAdmin(TranslationAdmin):
    list_display = ['name',]

@admin.register(Crd)
class CrdAdmin(TranslationAdmin):
    list_display = ['title', 'desc', 'button',]

    formfield_overrides = {
        models.TextField: {'widget': CKEditor5Widget(config_name='default')},
    }