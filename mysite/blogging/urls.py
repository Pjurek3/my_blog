from django.urls import path, include
from blogging.views import detail_view, list_view, PostViewSet, UserViewSet, CategoryViewSet
from rest_framework import routers
from blogging.feeds import LatestPostsFeed

router = routers.DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'users', UserViewSet)
router.register(r'categories', CategoryViewSet)

urlpatterns = [
    path("", list_view, name="blog_index"),
    path("api/", include(router.urls)),
    path("posts/<int:post_id>/", detail_view, name="blog_detail"),
    path('latest/feed/', LatestPostsFeed()),
]
