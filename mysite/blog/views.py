from django.shortcuts import render
from .models import Post
# Create your views here.
# add post
def add_post(request):
    if request.method == 'POST':
        content = request.POST.get('content')
        img = request.FILES.get('img')
        status = request.POST.get('status')
        
        post = Post(content=content,img=img,status=status)
        if post.is_valid():
            post.save()
            return render(request, 'index.html')
        else:
            # post = Post(content=content,img=img,status=status)
            print("error bro")
        
    return render(request, 'index.html')
