from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination, CursorPagination


class SmallPageNumberPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 5


class SmallLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 5
    limit_query_param = 'limit'
    offset_query_param = 'offset'
    max_limit = 5


class SmallCursorPagination(CursorPagination):
    ordering = '-pk'
    page_size = 3
