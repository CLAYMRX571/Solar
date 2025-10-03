from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import Museum, Ms, Mega, Supa

@admin.register(Museum)
class MuseumAdmin(TranslationAdmin):
    list_display = ['name',]

@admin.register(Ms)
class MsAdmin(TranslationAdmin):
    list_display = ['name', 'desc', 'button',]

@admin.register(Mega)
class MegaAdmin(TranslationAdmin):
    list_display = ['name',]

@admin.register(Supa)
class SupaAdmin(TranslationAdmin):
    list_display = ['name', 'desc', 'button',]
