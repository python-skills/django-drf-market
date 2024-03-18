from django.contrib import admin
from django.contrib.admin import register
from activity.models import Comment


@register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'directory', 'caption', 'reply_to')
