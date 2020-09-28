from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import Post


class BlogSitemap(Sitemap):
    priority = 0.6
    changefreq = 'weekly'

    def items(self):
        return Post.objects.filter(status=1)

    def lastmod(self,obj):
        return obj.updated_date
