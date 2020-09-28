from django.contrib.sitemaps import Sitemap
from django.urls import reverse


class WebsiteSitemap(Sitemap):
    priority = 0.8
    changefreq = 'monthly'

    def items(self):
        return ['index', 'about', 'contact']

    def location(self, item):
        return reverse(f"website:{item}")
