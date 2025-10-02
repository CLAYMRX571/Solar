from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import Board, Ses, Member, Bar, Car

@admin.register(Board)
class BoardAdmin(TranslationAdmin):
    list_display = ['desc',]

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