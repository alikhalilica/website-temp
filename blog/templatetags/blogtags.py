from django import template
from blog.models import Post,Category
from comment.models import Comment
from django.utils.html import strip_spaces_between_tags, strip_tags
from django.utils.text import Truncator
from django.utils import timezone

register = template.Library()

@register.inclusion_tag("blog/post_categories.html")
def show_blog_categories():
    posts = Post.objects.filter(status=1)
    categories = Category.objects.all()
    cat_dict={}
    for category in categories:
        count = posts.filter(category__name=category.name).count()
        cat_dict[category.name] = count #{"sports":12}
    return {"categories":cat_dict}

@register.inclusion_tag('blog/recent_posts.html')
def show_recent_posts(count=3):
    posts = Post.objects.filter(status=1,published_date__lte=timezone.now()).order_by("published_date")[:count]
    return {'posts':posts}

@register.simple_tag
def count_comment(slug):
    comments = Comment.objects.filter(url =slug,approved_comment = True).count()
    return comments

# use this as snippet or
# this: {{ page.body|striptags|truncatewords:50 }}
@register.filter(name='excerpt')
def excerpt_with_ptag_spacing(value, arg):
    try:
        limit = int(arg)
    except ValueError:
        return 'Invalid literal for int().'

    # remove spaces between tags
    value = strip_spaces_between_tags(value)

    # add space before each P end tag (</p>)
    value = value.replace("</p>"," </p>")
    value = value.replace("&quot","  ")
    # strip HTML tags
    value = strip_tags(value)

    # other usage: return Truncator(value).words(length, html=True, truncate=' see more')
    return Truncator(value).words(limit)
