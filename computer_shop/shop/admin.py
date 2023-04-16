from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import *


class CompElemAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'cat', 'price', 'time_create', 'get_html_photo', 'available')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('available', )
    list_filter = ('available', 'time_create')
    prepopulated_fields = {'slug': ('title', )}
    fields = ('title', 'slug', 'cat', 'content', 'photo', 'get_html_photo', 'available', 'time_create', 'time_update', 'price')
    readonly_fields = ('time_create', 'time_update', 'get_html_photo')

    def get_html_photo(self, object):
        if object.photo:
            return mark_safe(f'<img src="{object.photo.url}" width="50">')

    get_html_photo.short_description = 'Zdjęcia'


class CatCompElemAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name', )
    prepopulated_fields = {'slug': ('name', )}


admin.site.register(ComputerElems, CompElemAdmin)
admin.site.register(CatComputerElems, CatCompElemAdmin)
