from django import template
from comment.models import Comment
from comment.forms import CommentForm
from django.utils.html import strip_spaces_between_tags, strip_tags
from django.utils.text import Truncator
from django.utils import timezone


register = template.Library()


@register.simple_tag
def count_comment(absolute_url):
    comments = Comment.objects.filter(url=absolute_url,approved_comment = True).count()
    return comments


@register.inclusion_tag('comments/user_comment.html', takes_context=True)
def UserComment(context,absolute_url):
    comments = Comment.objects.filter(url=absolute_url,approved_comment=True,parent__isnull= True)
    form = CommentForm()
    return {'comments':comments,'form':form,'user': context['user'],'url':absolute_url,"messages":context['messages']}