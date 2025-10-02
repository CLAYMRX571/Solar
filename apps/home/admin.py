from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import Banner, Home, Messages, Latest, Slide, Slides

@admin.register(Banner)
class BannerAdmin(TranslationAdmin):
    list_display = ['name',]

@admin.register(Home)
class HomeAdmin(TranslationAdmin):
    list_display = ['name', 'desc', 'button_name', 'buttons_name', 'buttons_desc',]

@admin.register(Messages)
class MessagesAdmin(TranslationAdmin):
    list_display = ['name', 'title', 'desc', 'button',]

@admin.register(Latest)
class LatestAdmin(TranslationAdmin):
    list_display = ['name', 'title', 'desc', 'button',]

@admin.register(Slide)
class SlideAdmin(TranslationAdmin):
    list_display = ['name',]
    
@admin.register(Slides)
class SlidesAdmin(TranslationAdmin):
    list_display = ['name',]
    