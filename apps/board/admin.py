from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import Board

@admin.register(Board)
class BoardAdmin(TranslationAdmin):
    list_display = ['name', 'desc', 'board_desc',]