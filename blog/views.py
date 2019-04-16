from django.shortcuts import render
from . import models
from django.core.paginator import Paginator

# Create your views here.

def blog_list(request):
   
    blog_list_all = models.Blog.objects.all()
    paginator = Paginator(blog_list_all,1)  #每10页进行分页
    page_num = request.GET.get("page",1)  #获取页码参数(get请求)
    page_of_blogs = paginator.get_page(page_num)   
    blog_type_all = models.blog_type.objects.all()
 
    cur_page_num = page_of_blogs.number  #获取当前页、
    # page_range = [cur_page_num - 2,cur_page_num - 1,cur_page_num,cur_page_num + 1,cur_page_num +2]
    # page_range = filter(lambda x: 0 < x < paginator.num_pages,range(cur_page_num - 2 ,cur_page_num + 3))
    page_range = [ x for x in range(cur_page_num - 2,cur_page_num +3) if 0 < x < paginator.num_pages ]

    context = {}
    context['blog_list_all'] = page_of_blogs
    context['blog_type_all'] = blog_type_all
    context['page_range'] = page_range
    return render(request,'blog_list.html',context)

def index(request):
    return render(request,'index.html')


def blog_content(request,blog_id):
    blog = models.Blog.objects.get(id=blog_id)
    context = {}   
    context['blog'] = blog
    return render(request,'blog_content.html',context)


def blog_type(request,blog_with_type):
    blog_type_all = models.blog_type.objects.all()
    blog_type_mark = models.blog_type.objects.get(pk=blog_with_type)
    context = {}
    context['blog_type_all'] = blog_type_all
    context['blog_with_type'] = models.Blog.objects.filter(blog_type=blog_type_mark)
    return render(request,'blog_type.html',context)


