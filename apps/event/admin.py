from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import Event

@admin.register(Event)
class EventAdmin(TranslationAdmin):
    list_display = ['name', 'location', 'title',]