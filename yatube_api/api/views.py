from django.shortcuts import get_object_or_404

from rest_framework import filters, pagination, permissions, viewsets

from .permissions import IsAuthorOrReadOnlyPermission
from .serializers import (
    CommentSerializer,
    FollowSerializer,
    GroupSerializer,
    PostSerializer
)
from posts.models import Follow, Group, Post


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthorOrReadOnlyPermission,)
    pagination_class = pagination.LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (IsAuthorOrReadOnlyPermission,)

    def getting_post(self):
        return get_object_or_404(Post, pk=self.kwargs.get('post_id'))

    def get_queryset(self):
        return self.getting_post().comments

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, post=self.getting_post())


class FollowViewSet(viewsets.ModelViewSet):
    serializer_class = FollowSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('following__username',)

    def get_queryset(self):
        return Follow.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
