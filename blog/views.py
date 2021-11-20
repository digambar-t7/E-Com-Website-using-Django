from django.shortcuts import render
from django.http import HttpResponse
from .models import BlogPost

# Create your views here.
def home(request):
    posts = BlogPost.objects.all()
    return render(request,'blog/home.html',{'posts':posts})

def blogpost(request,id):
    post = BlogPost.objects.filter(post_id=id)
    return render(request,'blog/blogpost.html',{'post':post[0]})