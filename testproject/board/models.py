# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = True` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AllCost(models.Model):
    all_cost_pk = models.BigIntegerField(db_column='ALL_COST_PK', primary_key=True)  # Field name made lowercase.
    cost_type_cost_type_pk = models.ForeignKey('CostType', models.DO_NOTHING, db_column='COST_TYPE_COST_TYPE_PK')  # Field name made lowercase.
    all_cost_cost = models.PositiveIntegerField(db_column='ALL_COST_COST')  # Field name made lowercase.
    all_cost_nm = models.CharField(db_column='ALL_COST_NM', max_length=45)  # Field name made lowercase.
    all_cost_index = models.CharField(db_column='ALL_COST_INDEX', max_length=200, blank=True, null=True)  # Field name made lowercase.
    all_cost_craeted_dttm = models.DateTimeField(db_column='ALL_COST_CRAETED_DTTM')  # Field name made lowercase.
    all_cost_modifed_dttm = models.DateTimeField(db_column='ALL_COST_MODIFED_DTTM')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'ALL_COST'


class AllCostAndHousehold(models.Model):
    all_cost_all_cost_pk = models.OneToOneField(AllCost, models.DO_NOTHING, db_column='ALL_COST_ALL_COST_PK', primary_key=True)  # Field name made lowercase.
    household_household_pk = models.ForeignKey('Household', models.DO_NOTHING, db_column='HOUSEHOLD_HOUSEHOLD_PK')  # Field name made lowercase.
    bill_bill_pk = models.ForeignKey('Bill', models.DO_NOTHING, db_column='Bill_Bill_PK', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'ALL_COST_AND_HOUSEHOLD'
        unique_together = (('all_cost_all_cost_pk', 'household_household_pk'),)


class ApiRoute(models.Model):
    api_route_pk = models.AutoField(db_column='API_ROUTE_PK', primary_key=True)  # Field name made lowercase.
    api_route_path = models.CharField(db_column='API_ROUTE_PATH', max_length=45)  # Field name made lowercase.
    method_method_pk = models.ForeignKey('Method', models.DO_NOTHING, db_column='METHOD_METHOD_PK')  # Field name made lowercase.
    role_role_pk = models.ForeignKey('Role', models.DO_NOTHING, db_column='ROLE_ROLE_PK', blank=True, null=True)  # Field name made lowercase.
    service_service_pk = models.ForeignKey('Service', models.DO_NOTHING, db_column='SERVICE_SERVICE_PK')  # Field name made lowercase.
    api_route_gateway_refresh = models.IntegerField(db_column='API_ROUTE_GATEWAY_REFRESH', blank=True, null=True)  # Field name made lowercase.
    api_route_only_token = models.IntegerField(db_column='API_ROUTE_ONLY_TOKEN', blank=True, null=True)  # Field name made lowercase.
    api_route_optional = models.IntegerField(db_column='API_ROUTE_OPTIONAL', blank=True, null=True)  # Field name made lowercase.
    api_route_authorization = models.IntegerField(db_column='API_ROUTE_AUTHORIZATION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'API_ROUTE'


class Area(models.Model):
    area_pk = models.PositiveIntegerField(db_column='AREA_PK', primary_key=True)  # Field name made lowercase.
    area_size = models.PositiveIntegerField(db_column='AREA_SIZE')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'AREA'


class Board(models.Model):
    board_pk = models.PositiveIntegerField(db_column='BOARD_PK', primary_key=True)  # Field name made lowercase.
    board_write_role_role_pk = models.ForeignKey('Role', models.DO_NOTHING, db_column='BOARD_WRITE_ROLE_ROLE_PK', related_name='board_write_role_role_pk')  # Field name made lowercase.
    board_read_role_role_pk = models.ForeignKey('Role', models.DO_NOTHING, db_column='BOARD_READ_ROLE_ROLE_PK', related_name='board_read_role_role_pk')  # Field name made lowercase.
    board_comment_role_role_pk = models.ForeignKey('Role', models.DO_NOTHING, db_column='BOARD_COMMENT_ROLE_ROLE_PK', related_name='board_comment_role_role_pk')  # Field name made lowercase.
    board_index = models.CharField(db_column='BOARD_INDEX', max_length=100, blank=True, null=True)  # Field name made lowercase.
    board_hot_post_like = models.IntegerField(db_column='BOARD_HOT_POST_LIKE', blank=True, null=True)  # Field name made lowercase.
    layout_layout_pk = models.ForeignKey('Layout', models.DO_NOTHING, db_column='LAYOUT_LAYOUT_PK')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'BOARD'


class Building(models.Model):
    building_pk = models.CharField(db_column='BUILDING_PK', primary_key=True, max_length=3)  # Field name made lowercase.
    user_user_pk = models.ForeignKey('User', models.DO_NOTHING, db_column='USER_USER_PK', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'BUILDING'


class Bill(models.Model):
    bill_pk = models.PositiveBigIntegerField(db_column='Bill_PK', primary_key=True)  # Field name made lowercase.
    household_household_pk = models.ForeignKey('Household', models.DO_NOTHING, db_column='HOUSEHOLD_HOUSEHOLD_PK')  # Field name made lowercase.
    bill_cost = models.PositiveIntegerField(db_column='Bill_COST')  # Field name made lowercase.
    bill_craeted_dttm = models.CharField(db_column='Bill_CRAETED_DTTM', max_length=45, blank=True, null=True)  # Field name made lowercase.
    bill_modifed_dttm = models.CharField(db_column='Bill_MODIFED_DTTM', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Bill'


class Comment(models.Model):
    comment_pk = models.AutoField(db_column='COMMENT_PK', primary_key=True)  # Field name made lowercase.
    comment_parent_comment_comment_pk = models.ForeignKey('self', models.DO_NOTHING, db_column='COMMENT_PARENT_COMMENT_COMMENT_PK', blank=True, null=True, related_name='reply')  # Field name made lowercase.
    status = models.PositiveIntegerField(db_column='STATUS')  # Field name made lowercase.
    user_user_pk = models.ForeignKey('User', models.DO_NOTHING, db_column='USER_USER_PK')  # Field name made lowercase.
    post_post_pk = models.ForeignKey('Post', models.DO_NOTHING, db_column='POST_POST_PK')  # Field name made lowercase.

    comment_text = models.TextField(db_column='COMMENT_TEXT')
    comment_write_time = models.DateTimeField(db_column='COMMENT_WRITE_TIME', auto_now_add=True)

    class Meta:
        managed = True
        db_table = 'COMMENT'


class CostType(models.Model):
    cost_type_pk = models.IntegerField(db_column='COST_TYPE_PK', primary_key=True)  # Field name made lowercase.
    cost_type_nm = models.CharField(db_column='COST_TYPE_NM', unique=True, max_length=45)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'COST_TYPE'


class Household(models.Model):
    household_pk = models.AutoField(db_column='HOUSEHOLD_PK', primary_key=True)  # Field name made lowercase.
    household_unit = models.CharField(db_column='HOUSEHOLD_UNIT', max_length=4)  # Field name made lowercase.
    building_building_pk = models.ForeignKey(Building, models.DO_NOTHING, db_column='BUILDING_BUILDING_PK')  # Field name made lowercase.
    household_representative_user_user_pk = models.ForeignKey('User', models.DO_NOTHING, db_column='HOUSEHOLD_REPRESENTATIVE_USER_USER_PK', blank=True, null=True)  # Field name made lowercase.
    area_area_pk = models.ForeignKey(Area, models.DO_NOTHING, db_column='AREA_AREA_PK')  # Field name made lowercase.
    household_representative_account = models.CharField(db_column='HOUSEHOLD_REPRESENTATIVE_ACCOUNT', max_length=29, blank=True, null=True)  # Field name made lowercase.
    household_occupancy_dt = models.DateField(db_column='HOUSEHOLD_OCCUPANCY_DT', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'HOUSEHOLD'
        unique_together = (('household_unit', 'building_building_pk'),)


class Image(models.Model):
    image_pk = models.BigIntegerField(db_column='IMAGE_PK', primary_key=True)  # Field name made lowercase.
    post_post_pk = models.ForeignKey('Post', models.DO_NOTHING, db_column='POST_POST_PK')  # Field name made lowercase.
    image_location = models.CharField(db_column='IMAGE_LOCATION', unique=True, max_length=260)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'IMAGE'


class Layout(models.Model):
    layout_pk = models.IntegerField(db_column='LAYOUT_PK', primary_key=True)  # Field name made lowercase.
    layout_nm = models.CharField(db_column='LAYOUT_NM', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'LAYOUT'


class Like(models.Model):
    post_post_pk = models.ForeignKey('Post', models.DO_NOTHING, db_column='POST_POST_PK')  # Field name made lowercase.
    user_user_pk = models.ForeignKey('User', models.DO_NOTHING, db_column='USER_USER_PK')  # Field name made lowercase.
    like_create_dttm = models.DateTimeField(db_column='LIKE_CREATE_DTTM', blank=True, null=True, auto_now_add=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'LIKE'
        constraints = [models.UniqueConstraint(fields=('post_post_pk', 'user_user_pk'), name='unique-key-error')]


class Method(models.Model):
    method_pk = models.PositiveIntegerField(db_column='METHOD_PK', primary_key=True)  # Field name made lowercase.
    method_nm = models.CharField(db_column='METHOD_NM', unique=True, max_length=45)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'METHOD'


class ParkingInfo(models.Model):
    parking_info_pk = models.CharField(db_column='PARKING_INFO_PK', primary_key=True, max_length=50)  # Field name made lowercase.
    parking_info_last_parking_dttm = models.DateTimeField(db_column='PARKING_INFO_LAST_PARKING_DTTM', blank=True, null=True)  # Field name made lowercase.
    parking_info_status = models.IntegerField(db_column='PARKING_INFO_STATUS', blank=True, null=True)  # Field name made lowercase.
    parking_info_type_parking_info_type_pk = models.ForeignKey('ParkingInfoType', models.DO_NOTHING, db_column='PARKING_INFO_TYPE_PARKING_INFO_TYPE_PK')  # Field name made lowercase.
    parking_info_parking_info_floor_pk = models.ForeignKey('ParkingInfoFloor', models.DO_NOTHING, db_column='PARKING_INFO_PARKING_INFO_FLOOR_PK')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'PARKING_INFO'


class ParkingInfoFloor(models.Model):
    parking_info_floor_pk = models.IntegerField(db_column='PARKING_INFO_FLOOR_PK', primary_key=True)  # Field name made lowercase.
    parking_info_floor_nm = models.CharField(db_column='PARKING_INFO_FLOOR_NM', unique=True, max_length=50)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'PARKING_INFO_FLOOR'


class ParkingInfoType(models.Model):
    parking_info_type_pk = models.IntegerField(db_column='PARKING_INFO_TYPE_PK', primary_key=True)  # Field name made lowercase.
    parking_info_type_nm = models.CharField(db_column='PARKING_INFO_TYPE_NM', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'PARKING_INFO_TYPE'


class Pay(models.Model):
    pay_pk = models.BigIntegerField(db_column='PAY_PK', primary_key=True)  # Field name made lowercase.
    bill_bill_pk = models.ForeignKey(Bill, models.DO_NOTHING, db_column='Bill_Bill_PK')  # Field name made lowercase.
    pay_status_pay_status_pk = models.ForeignKey('PayStatus', models.DO_NOTHING, db_column='PAY_STATUS_PAY_STATUS_PK')  # Field name made lowercase.
    pay_created_dttm = models.DateTimeField(db_column='PAY_CREATED_DTTM', blank=True, null=True)  # Field name made lowercase.
    pay_modifed_dttm = models.DateTimeField(db_column='PAY_MODIFED_DTTM', blank=True, null=True)  # Field name made lowercase.
    pay_toss_code = models.CharField(db_column='PAY_TOSS_CODE', max_length=200, blank=True, null=True)  # Field name made lowercase.
    toss_pay_toss_pay_code = models.ForeignKey('TossPay', models.DO_NOTHING, db_column='TOSS_PAY_TOSS_PAY_CODE', related_name='toss_pay_toss_pay_code')  # Field name made lowercase.
    toss_pay_toss_pay_order = models.ForeignKey('TossPay', models.DO_NOTHING, db_column='TOSS_PAY_TOSS_PAY_ORDER_ID', related_name='toss_pay_toss_pay_order')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'PAY'


class PayStatus(models.Model):
    pay_status_pk = models.PositiveIntegerField(db_column='PAY_STATUS_PK', primary_key=True)  # Field name made lowercase.
    pay_status_nm = models.CharField(db_column='PAY_STATUS_NM', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'PAY_STATUS'


class PerCost(models.Model):
    per_cost_pk = models.BigIntegerField(db_column='PER_COST_PK', primary_key=True)  # Field name made lowercase.
    bill_bill_pk = models.ForeignKey(Bill, models.DO_NOTHING, db_column='Bill_Bill_PK', blank=True, null=True)  # Field name made lowercase.
    cost_type_cost_type_pk = models.ForeignKey(CostType, models.DO_NOTHING, db_column='COST_TYPE_COST_TYPE_PK')  # Field name made lowercase.
    household_household_pk = models.ForeignKey(Household, models.DO_NOTHING, db_column='HOUSEHOLD_HOUSEHOLD_PK')  # Field name made lowercase.
    per_cost_cost = models.CharField(db_column='PER_COST_COST', max_length=45, blank=True, null=True)  # Field name made lowercase.
    per_cost_modifed_dttm = models.DateTimeField(db_column='PER_COST_MODIFED_DTTM')  # Field name made lowercase.
    per_cost_craeted_dttm = models.DateTimeField(db_column='PER_COST_CRAETED_DTTM')  # Field name made lowercase.
    per_cost_nm = models.CharField(db_column='PER_COST_NM', max_length=45)  # Field name made lowercase.
    per_cost_index = models.CharField(db_column='PER_COST_INDEX', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'PER_COST'


class Post(models.Model):
    post_pk = models.BigAutoField(db_column='POST_PK', primary_key=True)  # Field name made lowercase.
    user_user_pk = models.ForeignKey('User', models.DO_NOTHING, db_column='USER_USER_PK', null=True)  # Field name made lowercase.
    post_text = models.TextField(db_column='POST_TEXT')  # Field name made lowercase.
    board_board_pk = models.ForeignKey(Board, models.DO_NOTHING, db_column='BOARD_BOARD_PK')  # Field name made lowercase.
    post_title = models.CharField(db_column='POST_TITLE', max_length=45, blank=True, null=True)  # Field name made lowercase.

    post_tag = models.IntegerField(db_column='POST_TAG', null=True)
    post_refer = models.ForeignKey('self', on_delete=models.DO_NOTHING, db_column='POST_REFER', null=True)
    post_write_time = models.DateTimeField(db_column='POST_WRITE_TIME', auto_now_add=True, null=False)
    post_update_time = models.DateTimeField(db_column='POST_UPDATE_TIME', auto_now=True, null=False)

    class Meta:
        managed = True
        db_table = 'POST'


class RegisterCode(models.Model):
    register_code_pk = models.CharField(db_column='REGISTER_CODE_PK', primary_key=True, max_length=36)  # Field name made lowercase.
    household_household_pk = models.ForeignKey(Household, models.DO_NOTHING, db_column='HOUSEHOLD_HOUSEHOLD_PK')  # Field name made lowercase.
    register_code_rep_user_name = models.CharField(db_column='REGISTER_CODE_REP_USER_NAME', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'REGISTER_CODE'


class Role(models.Model):
    role_pk = models.PositiveIntegerField(db_column='ROLE_PK', primary_key=True)  # Field name made lowercase.
    role_nm = models.CharField(db_column='ROLE_NM', unique=True, max_length=45)  # Field name made lowercase.
    role_kr_nm = models.CharField(db_column='ROLE_KR_NM', unique=True, max_length=45)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'ROLE'


class Service(models.Model):
    service_pk = models.PositiveIntegerField(db_column='SERVICE_PK', primary_key=True)  # Field name made lowercase.
    service_nm = models.CharField(db_column='SERVICE_NM', unique=True, max_length=45)  # Field name made lowercase.
    service_domain = models.CharField(db_column='SERVICE_DOMAIN', unique=True, max_length=45)  # Field name made lowercase.
    service_index = models.TextField(db_column='SERVICE_INDEX', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'SERVICE'


class TossPay(models.Model):
    toss_pay_code = models.CharField(db_column='TOSS_PAY_CODE', primary_key=True, max_length=200)  # Field name made lowercase.
    toss_pay_order_id = models.CharField(db_column='TOSS_PAY_ORDER_ID', max_length=64)  # Field name made lowercase.
    toss_pay_status_pay_status_pk = models.ForeignKey('TossPayStatus', models.DO_NOTHING, db_column='TOSS_PAY_STATUS_PAY_STATUS_PK')  # Field name made lowercase.
    toss_pay_method_toss_pay_method_pk = models.ForeignKey('TossPayMethod', models.DO_NOTHING, db_column='TOSS_PAY_METHOD_TOSS_PAY_METHOD_PK')  # Field name made lowercase.
    toss_pay_type_toss_pay_type_pk = models.ForeignKey('TossPayType', models.DO_NOTHING, db_column='TOSS_PAY_TYPE_TOSS_PAY_TYPE_PK')  # Field name made lowercase.
    toss_pay_order_name = models.CharField(db_column='TOSS_PAY_ORDER_NAME', max_length=45)  # Field name made lowercase.
    toss_pay_request_dttm = models.DateTimeField(db_column='TOSS_PAY_REQUEST_DTTM')  # Field name made lowercase.
    toss_pay_approved_dttm = models.DateTimeField(db_column='TOSS_PAY_APPROVED_DTTM')  # Field name made lowercase.
    toss_pay_transaction_key = models.CharField(db_column='TOSS_PAY_TRANSACTION_KEY', max_length=64)  # Field name made lowercase.
    toss_pay_last_transaction_key = models.CharField(db_column='TOSS_PAY_LAST_TRANSACTION_KEY', max_length=64)  # Field name made lowercase.
    toss_pay_cancels_transaction_key = models.CharField(db_column='TOSS_PAY_CANCELS_TRANSACTION_KEY', max_length=64, blank=True, null=True)  # Field name made lowercase.
    toss_pay_receipt = models.CharField(db_column='TOSS_PAY_RECEIPT', max_length=2000)  # Field name made lowercase.
    toss_pay_cash_receipt = models.CharField(db_column='TOSS_PAY_CASH_RECEIPT', max_length=2000, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'TOSS_PAY'
        unique_together = (('toss_pay_code', 'toss_pay_order_id'),)


class TossPayMethod(models.Model):
    toss_pay_method_pk = models.PositiveIntegerField(db_column='TOSS_PAY_METHOD_PK', primary_key=True)  # Field name made lowercase.
    toss_pay_method_nm = models.CharField(db_column='TOSS_PAY_METHOD_NM', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'TOSS_PAY_METHOD'


class TossPayStatus(models.Model):
    toss_pay_status_pk = models.PositiveIntegerField(db_column='TOSS_PAY_STATUS_PK', primary_key=True)  # Field name made lowercase.
    toss_pay_status_nm = models.CharField(db_column='TOSS_PAY_STATUS_NM', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'TOSS_PAY_STATUS'


class TossPayType(models.Model):
    toss_pay_type_pk = models.PositiveIntegerField(db_column='TOSS_PAY_TYPE_PK', primary_key=True)  # Field name made lowercase.
    toss_pay_type_nm = models.CharField(db_column='TOSS_PAY_TYPE_NM', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'TOSS_PAY_TYPE'


class User(models.Model):
    user_pk = models.CharField(db_column='USER_PK', primary_key=True, max_length=28)  # Field name made lowercase.
    user_phonenum = models.CharField(db_column='USER_PHONENUM', unique=True, max_length=11, blank=True, null=True)  # Field name made lowercase.
    user_email = models.CharField(db_column='USER_EMAIL', unique=True, max_length=256)  # Field name made lowercase.
    user_nm = models.CharField(db_column='USER_NM', max_length=45)  # Field name made lowercase.
    role_role_pk = models.ForeignKey(Role, models.DO_NOTHING, db_column='ROLE_ROLE_PK')  # Field name made lowercase.
    user_date_birth = models.DateField(db_column='USER_DATE_BIRTH', blank=True, null=True)  # Field name made lowercase.
    user_created_dttm = models.DateTimeField(db_column='USER_CREATED_DTTM', blank=True, null=True)  # Field name made lowercase.
    user_modified_dttm = models.DateTimeField(db_column='USER_MODIFIED_DTTM', blank=True, null=True)  # Field name made lowercase.
    household_household_pk = models.ForeignKey(Household, models.DO_NOTHING, db_column='HOUSEHOLD_HOUSEHOLD_PK')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'USER'


class VhclInfo(models.Model):
    vhcl_info_pk = models.CharField(db_column='VHCL_INFO_PK', primary_key=True, max_length=7)  # Field name made lowercase.
    vhcl_info_nm = models.CharField(db_column='VHCL_INFO_NM', max_length=100, blank=True, null=True)  # Field name made lowercase.
    vhcl_info_created_dttm = models.DateTimeField(db_column='VHCL_INFO_CREATED_DTTM', blank=True, null=True)  # Field name made lowercase.
    vhcl_info_modified_dttm = models.DateTimeField(db_column='VHCL_INFO_MODIFIED_DTTM', blank=True, null=True)  # Field name made lowercase.
    vhcl_info_visiting_vehicle = models.IntegerField(db_column='VHCL_INFO_VISITING_VEHICLE')  # Field name made lowercase.
    vhcl_type_vhcl_type_pk = models.ForeignKey('VhclType', models.DO_NOTHING, db_column='VHCL_TYPE_VHCL_TYPE_PK')  # Field name made lowercase.
    household_household_pk = models.ForeignKey(Household, models.DO_NOTHING, db_column='HOUSEHOLD_HOUSEHOLD_PK')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'VHCL_INFO'


class VhclInout(models.Model):
    vhcl_inout_pk = models.PositiveIntegerField(db_column='VHCL_INOUT_PK', primary_key=True)  # Field name made lowercase.
    vhcl_inout_dttm = models.DateTimeField(db_column='VHCL_INOUT_DTTM')  # Field name made lowercase.
    vhcl_inout_type = models.PositiveIntegerField(db_column='VHCL_INOUT_TYPE')  # Field name made lowercase.
    vhcl_info_vhcl_info_pk = models.ForeignKey(VhclInfo, models.DO_NOTHING, db_column='VHCL_INFO_VHCL_INFO_PK')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'VHCL_INOUT'


class VhclType(models.Model):
    vhcl_type_pk = models.PositiveIntegerField(db_column='VHCL_TYPE_PK', primary_key=True)  # Field name made lowercase.
    vhcl_type_nm = models.CharField(db_column='VHCL_TYPE_NM', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'VHCL_TYPE'


class View(models.Model):
    user_user_pk = models.OneToOneField(User, models.DO_NOTHING, db_column='USER_USER_PK', primary_key=True)  # Field name made lowercase.
    post_post_pk = models.ForeignKey(Post, models.DO_NOTHING, db_column='POST_POST_PK')  # Field name made lowercase.
    view_created_dttm = models.DateTimeField(db_column='VIEW_CREATED_DTTM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'VIEW'
        unique_together = (('user_user_pk', 'post_post_pk'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'django_migrations'
