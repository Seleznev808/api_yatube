from django.urls import include, path

from rest_framework import routers

from .views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet


v1_router = routers.DefaultRouter()
v1_router.register('posts', PostViewSet)
v1_router.register('groups', GroupViewSet)
v1_router.register('follow', FollowViewSet, basename='follow')
v1_router.register('comments', CommentViewSet, basename='comments')
v1_router.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='comments-list'
)
v1_router.register(
    r'posts/(?P<post_id>\d+)/comments/(?P<comment_id>\d+)$',
    CommentViewSet,
    basename='comments-detail'
)

urlpatterns = [
    path('v1/', include(v1_router.urls)),
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
]
