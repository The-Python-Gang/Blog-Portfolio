from django.shortcuts import render
from blog.models import Post

# Create your views here.

def post_list(request):
    template_name = 'post-list.html'
    posts = Post.objects.all()
    context = {
        'posts' : posts
    }
    return render(request, template_name, context)

def post_detail(request, id):
    template_name = 'post-detail.html'
    post = Post.objects.get(id=id)
    context = {
        'post': post
    }
    return render(request, template_name, context)

def devs(request):
    template_devs = 'developers.html'
    return render(request, template_devs)

def dev_id(request, id):
    template_dev = 'post-list.html'
    if (id == 0):
        template_dev = 'devs/leo.html'
    if (id == 1):
        template_dev = 'devs/max.html'
    if (id == 2):
        template_dev = 'devs/pedro.html'
    if (id == 3):
        template_dev = 'devs/richard.html'

    return render(request, template_dev)