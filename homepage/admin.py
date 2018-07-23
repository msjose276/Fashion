from django.contrib import admin
from .models import Topic
# Register your models here.


class TopicAdmin(admin.ModelAdmin):
    ordering = ['title']
    list_display = ['category','title','sub_title']

admin.site.register(Topic, TopicAdmin)