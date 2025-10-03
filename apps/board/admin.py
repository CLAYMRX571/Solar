from django.contrib import admin
from django.db import models
from django_ckeditor_5.widgets import CKEditor5Widget
from modeltranslation.admin import TranslationAdmin
from .models import Board, Ses, Member, Bar, Car

@admin.register(Board)
class BoardAdmin(TranslationAdmin):
    list_display = ['desc',]

    formfield_overrides = {
        models.TextField: {'widget': CKEditor5Widget(config_name='default')},
    }

@admin.register(Ses)
class SesAdmin(TranslationAdmin):
    list_display = ['name',]

@admin.register(Member)
class MemberAdmin(TranslationAdmin):
    list_display = ['name', 'title',]

@admin.register(Bar)
class BarAdmin(TranslationAdmin):
    list_display = ['name',]

@admin.register(Car)
class CarAdmin(TranslationAdmin):
    list_display = ['name', 'title',]