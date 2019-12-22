from django.contrib.syndication.views import Feed
from django.urls import reverse
from blogging.models import Post

class LatestPostsFeed(Feed):
    title = "latest posts feed"
    description = "Updates on changes to posts in the blog."
    link = "/blogging/"

    def items(self):
        return Post.objects.order_by('-created_date')[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.text

    def item_link(self, item):
        return reverse('blog_detail', args=[item.pk])