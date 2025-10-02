from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import Membership, Text, Board

@admin.register(Membership)
class MembershipAdmin(TranslationAdmin):
    list_display = ['name', 'desc', 'column_name', 'column_desc', 'column_button',]

@admin.register(Text)
class TextAdmin(TranslationAdmin):
    list_display = ['desc',]

@admin.register(Board)
class BoardAdmin(TranslationAdmin):
    list_display = ['name', 'desc', 'title', 'button',]
