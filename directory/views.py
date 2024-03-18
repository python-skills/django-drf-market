from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from rest_framework.authentication import SessionAuthentication
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.decorators import action

from activity.serializers import CommentListSerializer
from directory.models import Directory, Category
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets

from directory.serializers import DirectoryListSerializer, DirectoryDetailSerializer, CategoryListSerializer, \
    CategoryDetailSerializer
from lib.pagination import SmallPageNumberPagination


class DirectoryReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Directory.objects.all() \
                .prefetch_related('categories') \
                .prefetch_related('comments')
    # serializer_class = DirectoryDetailSerializer
    pagination_class = SmallPageNumberPagination

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = []
        else:
            permission_classes = []
        return [permission() for permission in permission_classes]

    def get_serializer_class(self):
        if self.action == 'list':
            return DirectoryDetailSerializer
        return DirectoryDetailSerializer

    @action(detail=True)
    def get_comments(self, request, *args, **kwargs):
        directory = self.get_object()
        queryset = directory.comments.all()
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = CommentListSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class CategoryListAPI(ListCreateAPIView):
    queryset =  Category.objects.actives().filter(parent=None).prefetch_related('children')
    serializer_class = CategoryListSerializer

    # def get(self, request, *args, **kwargs):
    #     records = Category.objects.actives().filter(parent=None).prefetch_related('children')
    #     serializer = CategoryListSerializer(records, many=True)
    #     return Response(serializer.data)


class CategoryDetailAPI(APIView):
    permission_classes = (IsAuthenticated, )
    # authentication_classes = (SessionAuthentication, JWTAuthentication)

    def get(self, request, pk, *args, **kwargs):
        record = get_object_or_404(Category.objects.prefetch_related('directory_set'), **{'pk':pk})
        serializer = CategoryDetailSerializer(record)
        return Response(serializer.data)


class DirectoryDetailAPI(RetrieveAPIView):
    queryset = Directory.objects.all()\
                .prefetch_related('categories')\
                .prefetch_related('comments')

    serializer_class = DirectoryDetailSerializer


class DirectoryListAPI(ListAPIView):
    permission_classes = (IsAuthenticated, )
    queryset = Directory.objects.all().prefetch_related('categories')
    serializer_class = DirectoryListSerializer

    # def get(self, request, *args, **kwargs):
    #     directories = Directory.objects.all().prefetch_related('categories')
    #     serializer = DirectoryListSerializer(directories, many=True)
    #     return Response(serializer.data, status=status.HTTP_202_ACCEPTED)


class CategoryListView(ListView):
    model = Category
    queryset = Category.objects.actives().filter(parent_id=None).prefetch_related('children')

    # def get_queryset(self):
    #     qs = super().get_queryset()
    #     return qs.prefetch_related('parent').prefetch_related('children')


class CategoryDetailView(DetailView):
    model = Category
    queryset = Category.objects.actives().prefetch_related('children')

    # def get_queryset(self):
    #     qs = super().get_queryset()
    #     return qs.prefetch_related('directory_set')


class DirectoryListView(ListView):
    model = Directory
    queryset = Directory.objects.actives()


class DirectoryDetailView(DetailView):
    model = Directory
    queryset = Directory.objects.actives()

    # def get_queryset(self):
    #     qs = super().get_queryset()
    #     return qs.prefetch_related('categories').filter(is_active=True)

    # template_name = 'startup/directory_detail.html'


def category_test(request):
    category = Category.objects.prefetch_related('directory_set').get(pk=1)
    directories = category.directory_set
    return HttpResponse(directories)

# def directory_list(request):
#     directories = Directory.objects.all()
#     context = {
#         'directories': directories
#     }
#     return render(request, 'startup/directory_list.html', context=context)
#
#
# def directory_show(request, pk):
#     try:
#         startup = Directory.objects.get(pk=pk)
#     except Directory.DoesNotExist:
#         raise Http404(f"Directory does not exist")
#     context = {
#         'startup': startup
#     }
#     return render(request, 'startup/directory_detail.html', context=context)
