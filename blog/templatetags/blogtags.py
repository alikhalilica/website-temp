from django import template
from blog.models import Post,Category
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
    posts = Post.objects.filter(status=1).order_by("created_date")[:count]
    return {'posts':posts}

