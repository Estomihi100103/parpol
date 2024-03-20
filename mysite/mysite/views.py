from django.shortcuts import render
from blog.models import Post

def index(request):
    posts=Post.objects.all()
    context = {
        'title': 'Home',
        'Posts': posts,
    }
    return render(request, 'index.html',context)



def profile(request):
    
    return render(request, 'profile.html')