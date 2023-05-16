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
