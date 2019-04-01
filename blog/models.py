from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# 博客分类表
class blog_type(models.Model):
    typename = models.CharField(max_length=32)
    def __str__(self):
        return self.typename

#博客表
class Blog(models.Model):
    title = models.CharField(max_length=32)
    blog_type = models.ForeignKey(blog_type,on_delete=models.DO_NOTHING)
    author = models.ForeignKey(User,on_delete=models.DO_NOTHING)
    content = models.TextField()
    create_time = models.DateTimeField(auto_now_add=True)
    last_updated_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-create_time']

