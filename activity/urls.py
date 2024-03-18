from django.urls import path

from activity.views import CommentListCreateAPIView, CommentRetrieveAPIView, UserCommentsListView

urlpatterns = [
    path('api/comments/', CommentListCreateAPIView.as_view(), name='comment-list-api'),
    path('api/comments/<int:pk>/', CommentRetrieveAPIView.as_view(), name='comment-show-api'),
    path('api/comments/user/<int:user_id>/', UserCommentsListView.as_view(), name='user-comments-list-api'),
    # path('api/comments/', CommentListAPIView.as_view(), name='comment-list-api'),
]