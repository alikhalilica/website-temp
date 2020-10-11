from django.shortcuts import render, get_object_or_404 ,HttpResponseRedirect
from comment.models import Comment
from django.http import HttpResponse 
from .models import Post,Category
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.utils import timezone


# Create your views here.
def list_post (request):
    posts = Post.objects.filter(status=1,published_date__lte=timezone.now()).order_by("-published_date")
    paginator = Paginator(posts,2)
    page = request.GET.get('page')
    try :
        posts=paginator.page(page)
    except PageNotAnInteger:
        posts= paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    context = {'posts':posts,'page':page}
    return render(request,"blog/post_list.html",context)

def single_post (request,post_slug):
    post = get_object_or_404(Post,slug = post_slug,status=1,published_date__lte=timezone.now())   
    context = {'post':post, "meta": post.as_meta()}
    return render(request,"blog/single_post.html",context)


