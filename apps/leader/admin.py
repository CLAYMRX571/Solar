from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import Leader

@admin.register(Leader)
class LeaderAdmin(TranslationAdmin):
    list_display = ['name', 'more_name', 'desc', 'title', 'title_desc', 'file_name',]