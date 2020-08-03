from django.shortcuts import render, get_object_or_404 ,HttpResponseRedirect
from comment.models import Comment
from django.http import HttpResponse 
from .models import Post,Category
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from comment.forms import BlogCommentForm
# Create your views here.
def list_post (request):
    posts = Post.objects.all().order_by("-created_date")
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
    post = get_object_or_404(Post,slug = post_slug,status=1)
    comments = Comment.objects.filter(url = post.slug,approved_comment = True,parent__isnull=True).order_by("created_date")

    if request.method=="POST":
        # comment has been added
        form = BlogCommentForm(data=request.POST)
        if form.is_valid():
            parent_obj = None
            # get parent comment id from hidden input
            try:
                # id integer e.g. 15
                parent_id = int(request.POST.get('parent_id'))
            except:
                parent_id = None
            # if parent_id has been submitted get parent_obj id
            if parent_id:
                parent_obj = Comment.objects.get(id=parent_id)
                # if parent object exist
                if parent_obj:
                    # create replay comment object
                    replay_comment = form.save(commit=False)
                    # assign parent_obj to replay comment
                    replay_comment.parent = parent_obj
            # normal comment
            # create comment object but do not save to database
            new_comment = form.save(commit=False)
            # assign ship to the comment
            new_comment.post = post
            # save
            new_comment.save()
            return HttpResponseRedirect(request.path_info)
    else :
        form = BlogCommentForm()
        context = {'post':post,'comments':comments,'form':form}
        return render(request,"blog/single_post.html",context)


