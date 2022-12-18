from datetime import datetime
import uuid

from django.db.models import Model, CharField, FilePathField, DateTimeField, TextField, UUIDField, IntegerField, \
    BooleanField, EmailField


# Create your models here.
class Agent(Model):
    """
    秘钥生成规则: md5(md5(password + timestamp) + salt)
    """
    _id = CharField(max_length=40, db_column="id", primary_key=True, verbose_name="ID", default=uuid.uuid4)
    secret_key = CharField(max_length=255, unique=True)
    ctime = DateTimeField(verbose_name="注册时间", default=datetime.now)
    utime = DateTimeField(verbose_name="最后一次更新时间")
    reg_reason = CharField(max_length=1024, default="自动发现并注册", verbose_name="注册方式")
    oper_id = CharField(max_length=40, verbose_name="操作人员ID")
    remarks = TextField(default="一般操作", verbose_name="备注")

    class Meta:
        db_table = "t_agent"

    def __str__(self):
        return self._id


class Config(Model):
    """
    抽象了 ini 格式的配置文件的存储方式
    例如将下面的 ini 配置：
    [section]
    key = value
    转换为：
    section.key = value
    """
    agent_id = CharField(max_length=40, verbose_name="代理工具ID(当该项为模板时,值为'--')", default="--")
    path = TextField(verbose_name="配置文件路径")
    section = CharField(max_length=255, verbose_name="配置段")
    key = CharField(max_length=255, verbose_name="配置键")
    value = CharField(max_length=1024, verbose_name="配置值")
    ctime = DateTimeField(verbose_name="创建时间", default=datetime.now)
    utime = DateTimeField(verbose_name="更新时间", default=datetime.now)
    oper_id = CharField(max_length=40, verbose_name="操作人ID")
    remarks = TextField(default="一般操作。", verbose_name="备注")
    is_template = BooleanField(default=False, verbose_name="是否为模板字段")

    class Meta:
        db_table = "t_config"


class ServiceConfig(Model):
    """
    Systemd Online 配置文件
    """
    _id = CharField(max_length=40, db_column="id", primary_key=True, verbose_name="ID", default=uuid.uuid4)
    cname = CharField(max_length=255, blank=True, verbose_name="别名")
    ctime = DateTimeField(verbose_name="创建时间", default=datetime.now)
    utime = DateTimeField(verbose_name="更新时间", default=datetime.now)

    class Meta:
        db_table = "t_server_config"


class ConfigTemplate(Model):
    """
    配置文件模板
    """
    _id = UUIDField(max_length=40, db_column="id", primary_key=True, verbose_name="ID", default=uuid.uuid4)
    name = CharField(max_length=255, verbose_name="名称")
    owner_id = CharField(max_length=40, verbose_name="拥有者ID")
    path = TextField(verbose_name="配置文件路径")
    salt = CharField(max_length=1024, verbose_name="Slat(AES加密)")

    class Meta:
        db_table = "t_config_template"


class LogItem(Model):
    _id = UUIDField(max_length=40, db_column="id", primary_key=True, verbose_name="ID", default=uuid.uuid4)
    name = CharField(max_length=1024, verbose_name="操作内容")
    oper_id = CharField(max_length=40, verbose_name="操作人ID")
    ctime = DateTimeField(verbose_name="操作时间")

    class Meta:
        db_table = "t_log_item"


class Operator(Model):
    _id = CharField(max_length=40, db_column="id", primary_key=True, verbose_name="ID", default=uuid.uuid4)
    name = CharField(max_length=128, verbose_name="姓名")
    no = CharField(max_length=128, verbose_name="工号")
    ctime = DateTimeField(verbose_name="操作时间")
    domain = CharField(max_length=1024, verbose_name="组织架构路径")
    username = CharField(max_length=255, verbose_name="用户名")
    password = CharField(max_length=255, verbose_name="密码(AES加密)")
    email = EmailField(max_length=255, verbose_name="工作邮箱")
    email_backup = EmailField(max_length=255, verbose_name="备用工作邮箱")
    phone = CharField(max_length=255, verbose_name="工作手机")
    ctime = DateTimeField(verbose_name="创建时间", default=datetime.now)
    utime = DateTimeField(verbose_name="更新时间", default=datetime.now)

    class Meta:
        db_table = "t_operator"


class Group(Model):
    _id = CharField(max_length=40, db_column="id", primary_key=True, verbose_name="ID", default=uuid.uuid4)
    name = CharField(max_length=128, verbose_name="组名")
    synopsis = TextField(blank=True, verbose_name="简介")
    ctime = DateTimeField(verbose_name="创建时间", default=datetime.now)
    utime = DateTimeField(verbose_name="更新时间", default=datetime.now)

    class Meta:
        db_table = "t_group"

    def __str__(self):
        self.synopsis = self.synopsis if len(self.synopsis) < 40 else self.synopsis[0:20] + "..."
        return "{} ({})".format(self.name, self.synopsis)


class OperatorGroupRef(Model):
    uid = CharField(max_length=40, db_column="uid", verbose_name="UID")
    gid = CharField(max_length=40, db_column="gid", verbose_name="GID")

    class Meta:
        db_table = "t_operator_group_ref"
