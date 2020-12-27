from django.contrib import admin
from .models import Story

class StoryAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "content",)

admin.site.register(Story, StoryAdmin)