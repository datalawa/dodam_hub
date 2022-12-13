
# Create your views here.
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework.response import Response
import rest_framework.status as status
from django.db.utils import IntegrityError

from .models import Board as BoardModel
from .models import Post as PostModel
from .models import Comment as CommentModel
from .models import Image as ImageModel
from .models import View as ViewModel
from .models import Like as LikeModel
from .models import Layout as LayoutModel
from .models import User as UserModel
from .models import Role as RoleModel

from .serializers import BoardSerializer
from .serializers import PostSerializer
from .serializers import CommentPostSerializer

from . serializers import PostUpdateSerializer

from .serializers import CommentSerializer
from .serializers import ImageSerializer
from .serializers import ViewSerializer
from .serializers import LikeSerializer
from .serializers import LayoutSerializer
from .serializers import UserSerializer
from .serializers import RoleSerializer
from .serializers import PostGetSerializer

from rest_framework import viewsets
from .pagination import PostPagination
from .pagination import CommentPagination

class BoardViewSet(viewsets.ModelViewSet):

    queryset = BoardModel.objects.all()
    serializer_class = BoardSerializer

class PostViewSet(viewsets.ModelViewSet):

    queryset = PostModel.objects.all().order_by('-post_write_time')
    serializer_class = PostSerializer
    pagination_class = PostPagination

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def list(self, request, *args, **kwargs):
        if 'board_board_pk' in request.query_params and int(request.query_params['board_board_pk']) == 3:
            queryset = self.set_filters(self.get_queryset().filter(post_tag__lt=3), request).order_by('-post_write_time')
        else:
            queryset = self.set_filters(self.get_queryset(), request).order_by('-post_write_time')
        total_count = queryset.count()

        page = self.paginate_queryset(queryset)

        if page is not None:
            serializer = PostGetSerializer(page, many=True)
            response = self.get_paginated_response(serializer.data)
            response_data = response.data.copy()
            response_data['total_count'] = total_count
            response_data['count'] = len(response_data['results'])
            response_data['count'] = len(response_data['results'])
            # print('queryset', response_data)
            response.data = response_data
            return response

        serializer = PostGetSerializer(queryset.order_by('-post_pk'), many=True)
        print(serializer.data)
        return Response(serializer.data)

    def set_filters(self, queryset, request):
        board_board_pk = request.query_params.get('board_board_pk', None)
        post_title = request.query_params.get('post_title', None)
        post_text = request.query_params.get('post_text', None)
        post_tag = request.query_params.get('post_tag', None)
        user_user_pk = request.query_params.get('user_user_pk', None)

        if board_board_pk is not None:
            queryset = queryset.filter(board_board_pk=board_board_pk)

        if post_title is not None:
            queryset = queryset.filter(post_title__contains=post_title)

        if post_tag is not None:
            queryset = queryset.filter(post_tag__contains=post_tag)

        if post_text is not None:
            queryset = queryset.filter(post_text__contains=post_text)

        if user_user_pk is not None:
            queryset = queryset.filter(user_user_pk=user_user_pk)

        return queryset

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = PostGetSerializer(instance)
        return Response(serializer.data)


class CommentViewSet(viewsets.ModelViewSet):

    queryset = CommentModel.objects.all()
    serializer_class = CommentSerializer
    pagination_class = CommentPagination

    def create(self, request, *args, **kwargs):
        print(request.data)
        serializer = CommentPostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def list(self, request, *args, **kwargs):
        queryset = self.set_filters(self.get_queryset(), request).filter(comment_parent_comment_comment_pk=None).order_by('comment_write_time')

        page = self.paginate_queryset(queryset)

        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)

        return Response(serializer.data)

    def set_filters(self, queryset, request):
        post_pk = request.query_params.get('post_post_pk', None)
        comment_text = request.query_params.get('comment_text', None)
        user_pk = request.query_params.get('user_user_pk', None)

        if post_pk is not None:
            queryset = queryset.filter(post_post_pk=post_pk)

        if comment_text is not None:
            queryset = queryset.filter(comment_text__contains=comment_text)

        if user_pk is not None:
            queryset = queryset.filter(user_user_pk=user_pk)

        return queryset

class ImageViewSet(viewsets.ModelViewSet):
    queryset = ImageModel.objects.all()
    serializer_class = ImageSerializer

class ViewViewSet(viewsets.ModelViewSet):
    queryset = ViewModel.objects.all()
    serializer_class = ViewSerializer

class LikeViewSet(viewsets.ModelViewSet):
    queryset = LikeModel.objects.all()
    serializer_class = LikeSerializer

    def create(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
        except IntegrityError as e:
            if eval(str(e))[0] == 1062:
                print(request.data['post_post_pk'])
                instance = self.get_queryset().filter(post_post_pk=int(request.data['post_post_pk']), user_user_pk=request.data['user_user_pk'])
                self.perform_destroy(instance)
                return Response(status=status.HTTP_204_NO_CONTENT)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(e, status=status.HTTP_400_BAD_REQUEST)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class LayoutViewSet(viewsets.ModelViewSet):
    queryset = LayoutModel.objects.all()
    serializer_class = LayoutSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer

class RoleViewSet(viewsets.ModelViewSet):
    queryset = RoleModel.objects.all()
    serializer_class = RoleSerializer
