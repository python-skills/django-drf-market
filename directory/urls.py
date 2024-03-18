from django.urls import path, include

from rest_framework.routers import SimpleRouter

from directory.views import DirectoryListView, DirectoryDetailView, CategoryListView, CategoryDetailView, category_test, \
    DirectoryListAPI, DirectoryDetailAPI, CategoryListAPI, CategoryDetailAPI, DirectoryReadOnlyViewSet

# from

# directory_viewset_list = DirectoryReadOnlyViewSet.as_view({'get': 'list'})
# directory_viewset_retrive = DirectoryReadOnlyViewSet.as_view({'get': 'retrieve'})

router = SimpleRouter()
router.register('', DirectoryReadOnlyViewSet, 'directory-viewset')


urlpatterns = [
    # path('', directory_list, name='startup-list'),
    # path('<int:pk>/', directory_show, name='startup-show'),

    path('categories/test/', category_test, name='category-test'),
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),
    path('api/categories/', CategoryListAPI.as_view(), name='category-api-list'),
    path('api/categories/<int:pk>/', CategoryDetailAPI.as_view(), name='category-api-detail'),

    path('api/', DirectoryListAPI.as_view(), name='directory-api-list'),
    path('api/<int:pk>/', DirectoryDetailAPI.as_view(), name='directory-api-detail'),
    path('', DirectoryListView.as_view(), name='directory-list'),
    path('<int:pk>/', DirectoryDetailView.as_view(), name='directory-detail'),

    path('directory_viewset/', include(router.urls)),
    # path('directory_viewset/', directory_viewset_list, name='directory-viewset-list'),
    # path('directory_viewset/<int:pk>/', directory_viewset_retrive, name='directory-viewset-retrieve'),
]
