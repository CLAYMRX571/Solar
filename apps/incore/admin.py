from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import Incore, Core, Tess

@admin.register(Incore)
class IncoreAdmin(TranslationAdmin):
    list_display = ['name',]

@admin.register(Core)
class CoreAdmin(TranslationAdmin):
    list_display = ['name', 'desc', 'core_name', 'core_desc',]

@admin.register(Tess)
class TessAdmin(TranslationAdmin):
    list_display = ['name', 'desc',]
