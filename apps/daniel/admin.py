from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import Daniel

@admin.register(Daniel)
class DanielAdmin(TranslationAdmin):
    list_display = ['name', 'desc', 'eco_desc',]