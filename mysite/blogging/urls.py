from django.urls import path, include
from blogging.views import detail_view, list_view, PostViewSet, UserViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    path("", list_view, name="blog_index"),
    path("api/", include(router.urls)),
    path("posts/<int:post_id>/", detail_view, name="blog_detail"),
]
