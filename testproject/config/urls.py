"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from board.views import BoardViewSet
from board.views import PostViewSet
from board.views import CommentViewSet
from board.views import ImageViewSet
from board.views import ViewViewSet
from board.views import LikeViewSet
from board.views import LayoutViewSet
from board.views import UserViewSet
from board.views import RoleViewSet


# Board 목록 보여주기
board_list = BoardViewSet.as_view({
    'get': 'list',
    #'post': 'create',
})

# Board detail 보여주기
board_detail = BoardViewSet.as_view({
    'get': 'retrieve',
    #'put': 'update',
    #'delete': 'destroy'
})

post_list = PostViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

post_detail = PostViewSet.as_view({
    'get': 'retrieve',
    'patch': 'partial_update',
    'delete': 'destroy'
})

comment_list = CommentViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

comment_detail = CommentViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'delete': 'destroy'
})

image_list = ImageViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

image_detail = ImageViewSet.as_view({
    'get': 'retrieve',
    'delete': 'destroy'
})

view_list = ViewViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

view_detail = ViewViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'delete': 'destroy'
})

like_list = LikeViewSet.as_view({
    'get': 'list',
    'post': 'create',
})
#좋아요는 속성 변경 없으므로 put/update 하지 않음

like_detail = LikeViewSet.as_view({
    'get': 'retrieve',
    'delete': 'destroy'
})

layout_list = LayoutViewSet.as_view({
    'get': 'list',
    'post': 'create',
    'put': 'update',
})

layout_detail = LayoutViewSet.as_view({
    'get': 'retrieve',
    'delete': 'destroy'
})

user_list = UserViewSet.as_view({
    'get': 'list',
    'post': 'create',
    'put': 'update',
})

user_detail = UserViewSet.as_view({
    'get': 'retrieve',
    'delete': 'destroy'
})

role_list = RoleViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

role_detail = RoleViewSet.as_view({
    'get': 'retrieve',
    'delete': 'destroy'
})

urlpatterns = [
    path('hub/admin/', admin.site.urls),
    path('hub/board/', board_list),
    path('hub/board/<int:pk>/', board_detail),
    path('hub/board/post/', post_list),
    path('hub/board/post/<int:pk>/', post_detail),
    path('hub/board/post/comment/', comment_list),
    path('hub/board/post/comment/<int:pk>/', comment_detail),
    path('hub/board/post/image/', image_list),
    path('hub/board/post/image/<int:pk>/', image_detail),
    path('hub/board/post/view', view_list),
    path('hub/board/post/view/<int:pk>/', view_detail),
    path('hub/board/post/like/', like_list),
    path('hub/board/post/like/<int:pk>/', like_detail),
    path('hub/layout/', layout_list),
    path('hub/layout/<int:pk>/', layout_detail),
    path('hub/user/', user_list),
    path('hub/user/<int:pk>/', user_detail),
    path('hub/role/', role_list),
    path('hub/role/<int:pk>/', role_detail),
]


