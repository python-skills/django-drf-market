from rest_framework import serializers

from activity.serializers import CommentListSerializer
from directory.models import Directory, Category


class CategoryListSerializer(serializers.ModelSerializer):
    children = serializers.SerializerMethodField()
    parent = None

    class Meta:
        model = Category
        fields = ('id', 'name', 'logo', 'children', 'parent')

    def get_children(self, obj):
        if obj.children is not None:
            return CategoryListSerializer(obj.children, many=True).data
        else:
            return None


class CategoryDetailSimpleSerializer(serializers.ModelSerializer):
    parent = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ('id', 'name', 'logo', 'parent')

    def get_parent(self, obj):
        if obj.parent is not None:
            return CategoryDetailSimpleSerializer(obj.parent).data
        else:
            return None


class DirectoryListSerializer(serializers.ModelSerializer):
    categories = serializers.SerializerMethodField()

    class Meta:
        model = Directory
        fields = ('id', 'name', 'slug', 'logo', 'description', 'link', 'categories')

    def get_categories(self, obj):
        return ", ".join([category.name for category in obj.categories.all()])


class CategoryDetailSerializer(serializers.ModelSerializer):
    children = CategoryListSerializer(many=True)
    directory_set = DirectoryListSerializer(many=True)
    parent = CategoryDetailSimpleSerializer()

    class Meta:
        model = Category
        fields = ('id', 'name', 'logo', 'parent', 'children', 'directory_set')


class DirectoryDetailSerializer(serializers.ModelSerializer):
    categories = CategoryListSerializer(many=True)
    # comments = CommentListSerializer(many=True)
    comments = serializers.SerializerMethodField()

    class Meta:
        model = Directory
        fields = ('id', 'name', 'slug', 'logo', 'description', 'link', 'comments', 'categories')

    def get_comments(self, obj):
        serializer = CommentListSerializer(obj.comments.filter(reply_to__isnull=True), many=True)
        return serializer.data

class DirectoryDetailLiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Directory
        fields = ('id', 'name', 'slug', 'logo', 'link')
