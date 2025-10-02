from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import Leader, Cont, Win

@admin.register(Leader)
class LeaderAdmin(TranslationAdmin):
    list_display = ['name', 'desc',]

@admin.register(Cont)
class ContAdmin(TranslationAdmin):
    list_display = ['name', 'desc',]

@admin.register(Win)
class WinAdmin(TranslationAdmin):
    list_display = ['name', 'desc',]