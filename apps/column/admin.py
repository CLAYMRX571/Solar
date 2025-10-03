from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import Column, Data, Mons

@admin.register(Column)
class ColumnAdmin(TranslationAdmin):
    list_display = ['name', 'desc',]

@admin.register(Data)
class DataAdmin(TranslationAdmin):
    list_display = ['name',]

@admin.register(Mons)
class MonsAdmin(TranslationAdmin):
    list_display = ['name',]