import uuid

from django.db.models import Model, CharField, FilePathField, DateTimeField, TextField, UUIDField


# Create your models here.
class Agent(Model):
    pass


class Config(Model):
    """
    抽象了 ini 格式的配置文件的存储方式
    例如将下面的 ini 配置：
    [section]
    key = value
    转换为：
    section.key = value
    """

    server_id = CharField(max_length=40, verbose_name="服务器ID")
    path = FilePathField(verbose_name="配置文件路径")
    section = CharField(max_length=255, verbose_name="配置段")
    key = CharField(max_length=255, verbose_name="配置键")
    value = CharField(max_length=1024, verbose_name="配置值")
    ctime = DateTimeField(verbose_name="创建时间")
    utime = DateTimeField(verbose_name="更新时间")
    oper = CharField(max_length=40, verbose_name="操作人ID")
    remarks = TextField(default="一般操作。", verbose_name="备注")

    db_table = "t_config"

    class Server(Model):
        _id = UUIDField(max_length=40, db_column="id", primary_key=True, verbose_name="ID", default=uuid.uuid4())

        db_table = "t_server"

