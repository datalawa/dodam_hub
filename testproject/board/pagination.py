from rest_framework.pagination import PageNumberPagination

class PostPagination(PageNumberPagination):
    # pagination 구현 파트: page_size_query_param 값에 따라서 크기 결정, "page_size"로 설정하면 가변으로 설정 가능
    page_size = 5
    page_size_query_param = 'page_size'

class CommentPagination(PageNumberPagination):
    page_size = 50
    page_size_query_param = 'page_size'