from django.shortcuts import render
from django.views.generic import ListView, DetailView
from . models import BlogModel

# Create your views here.
# def blog(request):
#     return render(request, 'blog.html',{})

class BlogView(ListView):
    model = BlogModel
    template_name = 'blog.html'
    
class BlogDetailed(DetailView):
    model = BlogModel
    template_name = 'blog_detailed.html'
    context_object_name = 'post'