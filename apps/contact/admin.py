from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import Contact

@admin.register(Contact)
class ContactAdmin(TranslationAdmin):
    list_display = ['name', 'desc', 'adverb_desc', 'adverb_more',]
