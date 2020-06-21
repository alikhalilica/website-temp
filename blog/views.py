from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def list_post (request):
    return render(request,"blog/post_list.html")

def single_post (request):
    return render(request,"blog/single_post.html")


# Create your views here.
