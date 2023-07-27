from rest_framework.pagination import PageNumberPagination


class DataPaginator(PageNumberPagination):
    page_size = 10