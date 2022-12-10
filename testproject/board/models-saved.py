from django.db import models
from django.conf import settings

# Create your models here.

class Board(models.Model):
    board_pk = models.AutoField(db_column='BOARD_PK', primary_key=True)

    board_write_role = models.ForeignKey("board.Role", related_name='write',
                                         on_delete=models.DO_NOTHING, db_column='BOARD_WRITE_ROLE')
    board_read_role = models.ForeignKey("board.Role", related_name='read',
                                        on_delete=models.DO_NOTHING, db_column='BOARD_READ_ROLE')
    board_comment_role = models.ForeignKey("board.Role", related_name='comment',
                                           on_delete=models.DO_NOTHING, db_column='BOARD_COMMENT_ROLE')

    board_index = models.CharField(db_column='BOARD_ID_PK', max_length=200)
    board_hot_post_like = models.IntegerField(db_column='BOARD_HOT_POST_LIKE')
    layout_pk = models.ForeignKey("board.Layout", models.DO_NOTHING, db_column='LAYOUT_PK',null=True)


class Post(models.Model):
    post_pk = models.AutoField(db_column='POST_PK', primary_key=True)
    # on_delete를 models.DO_NOTHING
    user_user_pk = models.ForeignKey("board.User", on_delete=models.DO_NOTHING, db_column='USER_PK')
    board_board_pk = models.ForeignKey(Board, on_delete=models.DO_NOTHING, db_column='BOARD_PK')

    post_title = models.CharField(db_column='POST_TITLE', max_length=45)
    post_text = models.TextField(db_column='POST_TEXT')

    post_tag = models.CharField(db_column='POST_TAG', max_length=20,null=True,blank=True)
    post_refer = models.ForeignKey('self', on_delete=models.DO_NOTHING, db_column='POST_REFER',null=True)

    post_write_time = models.DateTimeField(db_column='POST_WRITE_TIME',auto_now_add=True)
    post_update_time = models.DateTimeField(db_column='POST_UPDATE_TIME',auto_now=True)

class Comment(models.Model):
    comment_pk = models.AutoField(db_column='COMMENT_PK', primary_key=True)

    user_pk = models.ForeignKey("board.User", on_delete=models.DO_NOTHING, db_column='USER_PK')
    post_pk = models.ForeignKey(Post, on_delete=models.DO_NOTHING, db_column='BOARD_PK')

    comment_text = models.CharField(db_column='COMMENT_TEXT', max_length=120)

    comment_status = models.BooleanField(db_column='COMMENT_STATUS')
    parent = models.ForeignKey('self', related_name='reply', on_delete=models.CASCADE,
                                          db_column='COMMENT_PARENT_PK',null=True,blank=True)

    comment_write_time = models.DateTimeField(db_column='COMMENT_WRITE_TIME', auto_now_add=True)

class Image(models.Model):
    image_pk = models.AutoField(db_column='IMAGE_PK', primary_key=True)
    post_pk = models.ForeignKey(Post, on_delete=models.DO_NOTHING, db_column='BOARD_PK')

    image_location = models.CharField(db_column='IMAGE_LOCATION', max_length=120)
class View(models.Model):
    user_pk = models.ForeignKey("board.User", on_delete=models.DO_NOTHING, db_column='USER_PK')
    post_pk = models.ForeignKey(Post, on_delete=models.DO_NOTHING, db_column='BOARD_PK')

    view_created_time = models.DateTimeField(db_column='VIEW_CREATED_TIME')


class Like(models.Model):
    user_pk = models.ForeignKey("board.User", on_delete=models.DO_NOTHING, db_column='USER_PK')
    post_pk = models.ForeignKey(Post, on_delete=models.DO_NOTHING, db_column='BOARD_PK')

    like_created_time = models.DateTimeField(db_column='LIKE_CREATED_TIME')


class Layout(models.Model):
    layout_pk = models.AutoField(db_column='LAYOUT_PK', primary_key=True)

    layout_name = models.CharField(db_column='LAYOUT_NAME', max_length=45)


class User(models.Model):
    user_pk = models.AutoField(db_column='USER_PK', primary_key=True)
    role_pk = models.ForeignKey("board.Role", on_delete=models.DO_NOTHING, db_column='ROLE_PK')


class Role(models.Model):
    role_pk = models.AutoField(db_column='ROLE_PK', primary_key=True)

    role_name = models.CharField(db_column='ROLE_NAME', max_length=45)
