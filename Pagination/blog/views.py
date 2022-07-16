from typing import Optional
from django.shortcuts import render,redirect
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView
from blog.models import Blog
from blog.forms import AddBlogForm
# Create your views here.
class Home(TemplateView):
    template_name: str = "blog/home.html"

class AddBlog(CreateView):
    model = Blog
    fields = ['title','desc']
    template_name: str = 'blog/add_blog.html'
    success_url: Optional[str] = '/create/'
    # def get_context_data(self, *args,**kwargs):
    #     context = super().get_context_data(*args,**kwargs)
    #     context['data'] = "hello"
    #     return context

        
    