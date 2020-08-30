from django.shortcuts import render
from comment.forms import CommentForm
from comment.models import Comment
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib import messages
from django.shortcuts import redirect
# Create your views here.
def CreateComment (request):
    if request.method=="POST":
    # comment has been added
        form = CommentForm(data=request.POST)
        if form.is_valid():
            #print("valid")
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
            new_comment.save()
            messages.success(request, 'your comment has been recieved waiting for confirmation') 
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            messages.error(request, 'problem setting your comment') 
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            #print("not valid")
