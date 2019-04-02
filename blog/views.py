from django.shortcuts import render
from . import models

# Create your views here.

def blog_list(request):
    blog_list_all = models.Blog.objects.all()
    blog_type_all = models.blog_type.objects.all()
    context = {}
    context['blog_list_all'] = blog_list_all
    context['blog_type_all'] = blog_type_all
    return render(request,'blog_list.html',context)

def index(request):
    return render(request,'index.html')


def blog_content(request,blog_id):
    blog = models.Blog.objects.get(id=blog_id)
    context = {}   
    context['blog'] = blog
    return render(request,'blog_content.html',context)
