from rest_framework import serializers
from activity.models import Comment


class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('caption', 'directory', 'reply_to')

    def validate_reply_to(self, attr):
        if attr.reply_to is not None:
            raise ValueError("You can not reply to a reply recursively")
        return attr

    def validate(self, attrs):
        return attrs


class CommentUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('caption', )


class CommentDetailSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.username')

    class Meta:
        model = Comment
        fields = ('id', 'caption', 'user', 'reply_to')


class CommentRepliesListSerializer(serializers.ModelSerializer):
    # reply_to = CommentDetailSerializer()
    user = serializers.CharField(source='user.username')

    class Meta:
        model = Comment
        fields = ('id', 'caption', 'user', 'reply_to')


class CommentListSerializer(serializers.ModelSerializer):
    # replies = CommentRepliesListSerializer(many=True)
    replies = serializers.SerializerMethodField()
    user = serializers.CharField(source='user.username')

    class Meta:
        model = Comment
        fields = ('id', 'caption', 'user', 'replies')

    def get_replies(self, obj):
        qs = obj.replies.all()

        if qs.count() > 10:
            qs = qs[:10]

        serializer = CommentRepliesListSerializer(qs, many=True)
        return serializer.data
