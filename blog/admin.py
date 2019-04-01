from django.contrib import admin
from .models import *

@admin.register(blog_type)
class blog_typeAdmin(admin.ModelAdmin):
    list_display = ('id','typename')

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title','blog_type','author','create_time','last_updated_time')


