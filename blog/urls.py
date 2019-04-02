from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.blog_list,name='blog_list'),
    path('<int:blog_id>',views.blog_content,name='blog_content'),
    path('pan/<int:blog_with_type>',views.blog_type,name='blog_type')
]
