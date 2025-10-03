from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import Public, Pub

@admin.register(Public)
class PublicAdmin(TranslationAdmin):
    list_display = ['name', 'desc', 'topic', 'link',]

@admin.register(Pub)
class PubAdmin(TranslationAdmin):
    list_display = ['name', 'desc', 'button',]