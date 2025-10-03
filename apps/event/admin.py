from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import Event, Text, Greeb

@admin.register(Event)
class EventAdmin(TranslationAdmin):
    list_display = ['name', 'desc', 'area', 'part', 'contact',]

@admin.register(Text)
class TextAdmin(TranslationAdmin):
    list_display = ['name',]

@admin.register(Greeb)
class GreebAdmin(TranslationAdmin):
    list_display = ['name', 'desc', 'button',]