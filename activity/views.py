from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView, RetrieveUpdateAPIView, \
    RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated

from activity.models import Comment
from activity.serializers import CommentCreateSerializer, CommentListSerializer, CommentUpdateSerializer
from lib.pagination import SmallPageNumberPagination, SmallLimitOffsetPagination, SmallCursorPagination
from lib.permissions import CommentListSeen, CommentRetrieveSeen
from rest_framework import throttling


class CommentListCreateAPIView(ListCreateAPIView):
    queryset = Comment.objects.filter(reply_to__isnull=True).select_related('user', 'directory', 'reply_to')
    serializer_class = CommentCreateSerializer
    permission_classes = (IsAuthenticated, )
    pagination_class = SmallCursorPagination
    throttle_scope = 'custom'

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return CommentListSerializer
        return self.serializer_class


class CommentRetrieveAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentListSerializer
    permission_classes = (IsAuthenticated, CommentRetrieveSeen)

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return self.serializer_class
        return CommentUpdateSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        # qs = qs.filter(user=self.request.user) # this line managed in CommentRetrieveSeen
        if self.request.method == 'DELETE':
            qs = qs.filter(replies__isnull=True)
        return qs


class UserCommentsListView(ListAPIView):
    queryset = Comment.objects.all()
    lookup_url_kwarg = 'user_id'
    serializer_class = CommentListSerializer
    pagination_class = SmallCursorPagination
    permission_classes = (IsAuthenticated, CommentListSeen)

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(user_id=self.kwargs[self.lookup_url_kwarg])


#
# class CommentListAPIView(ListAPIView):
#     queryset = Comment.objects.all().select_related('user', 'directory', 'reply_to')
#     serializer_class = CommentListSerializer
#     permission_classes = (IsAuthenticated, )
