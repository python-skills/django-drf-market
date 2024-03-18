from django.contrib import admin
from django.contrib.admin import register
from directory.models import Category, Directory


@register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_directories_count', 'parent', 'logo', 'is_active', 'modified_time')
    list_filter = ('is_active', )
    search_fields = ('name', 'is_active', 'parent__name')
    list_editable = ('is_active',)


@register(Directory)
class DirectoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_categories', 'slug', 'is_active', 'logo', 'modified_time')
    list_filter = ('is_active', )
    search_fields = ('name', 'slug', 'is_active')
    list_editable = ('is_active', )
