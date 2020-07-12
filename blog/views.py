from django.shortcuts import render
from django.http import HttpResponse
from .models import Post,Category

# Create your views here.
def list_post (request):
    posts = Post.objects.all().order_by("-created_date")
    context = {'posts':posts}
    return render(request,"blog/post_list.html",context)

def single_post (request,post_slug):
    return render(request,"blog/single_post.html")


# Create your views here.
