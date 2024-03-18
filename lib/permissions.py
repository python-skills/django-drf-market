from rest_framework.permissions import BasePermission


class CommentListSeen(BasePermission):
    # message = ""

    def has_permission(self, request, view):
        return request.user.id == view.kwargs['user_id']


class CommentRetrieveSeen(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.id == obj.user_id
