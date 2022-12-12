from rest_framework import serializers
from .models import Board as BoardModel
from .models import Post as PostModel
from .models import Comment as CommentModel
from .models import Image as ImageModel
from .models import View as ViewModel
from .models import Like as LikeModel
from .models import Layout as LayoutModel
from .models import User as UserModel
from .models import Role as RoleModel



class UserPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ['user_pk', 'user_email', 'user_nm']






class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = BoardModel
        fields = "__all__"

class PostUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostModel
        exlcude = ['post_pk','post_write_time','post_update_time']


class RecursiveSerializer(serializers.Serializer):
    def to_representation(self, instance):
        serializer = self.parent.parent.__class__(instance, context=self.context)
        return serializer.data


class CommentSerializer(serializers.ModelSerializer):
    reply = serializers.SerializerMethodField()
    # reply = RecursiveSerializer(many=True, read_only=True)
    post_post_pk = serializers.SlugRelatedField(queryset=PostModel.objects.all(), slug_field='post_pk')
    user_user_pk = UserPostSerializer(read_only=True)

    class Meta:
        model = CommentModel
        fields = "__all__"

    def get_reply(self, instance):
        # recursive
        serializer = self.__class__(instance.reply, many=True)
        serializer.bind('', self)
        return serializer.data

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageModel
        fields = "__all__"
class ViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = ViewModel
        fields = "__all__"
class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = LikeModel
        fields = "__all__"
class LayoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = LayoutModel
        fields = "__all__"
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = "__all__"
class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoleModel
        fields = "__all__"






class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostModel
        fields = "__all__"

class PostAnswerSerializer(serializers.ModelSerializer):
    user_user_pk = UserPostSerializer(read_only=True)
    like_count = serializers.SerializerMethodField()
    class Meta:
        model = PostModel
        fields = ['post_pk', 'user_user_pk', 'post_text',
                  'post_title', 'post_write_time', 'post_update_time', 'like_count']

class PostGetSerializer(serializers.ModelSerializer):
    user_user_pk = UserPostSerializer(read_only=True)
    like_count = serializers.SerializerMethodField()
    comment_count = serializers.SerializerMethodField()
    view_count = serializers.SerializerMethodField()
    post_refer = PostAnswerSerializer(read_only=True)

    def get_like_count(self, obj):
        return LikeModel.objects.filter(post_post_pk=obj.post_pk).count()

    def get_comment_count(self, obj):
        return CommentModel.objects.filter(post_post_pk=obj.post_pk).count()

    def get_view_count(self, obj):
        return ViewModel.objects.filter(post_post_pk=obj.post_pk).count()

    class Meta:
        model = PostModel
        fields = ['post_pk', 'user_user_pk', 'post_text', 'board_board_pk',
                  'post_title', 'post_tag', 'post_refer', 'post_write_time', 'post_update_time', 'like_count', 'comment_count', 'view_count']
