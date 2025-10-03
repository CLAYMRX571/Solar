from django.contrib import admin
from django.db import models
from django_ckeditor_5.widgets import CKEditor5Widget
from modeltranslation.admin import TranslationAdmin
from .models import Membership, Text, Board

@admin.register(Membership)
class MembershipAdmin(TranslationAdmin):
    list_display = ['name', 'desc', 'column_name', 'column_desc', 'column_button',]

    formfield_overrides = {
        models.TextField: {'widget': CKEditor5Widget(config_name='default')},
    }

@admin.register(Text)
class TextAdmin(TranslationAdmin):
    list_display = ['desc',]

    formfield_overrides = {
        models.TextField: {'widget': CKEditor5Widget(config_name='default')},
    }

@admin.register(Board)
class BoardAdmin(TranslationAdmin):
    list_display = ['name', 'desc', 'title', 'button',]

    formfield_overrides = {
        models.TextField: {'widget': CKEditor5Widget(config_name='default')},
    }
