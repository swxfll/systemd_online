from django.contrib import admin
from app.models import *


# Register your models here.
# 为每个 model 创建 admin 类

@admin.register(Agent)
class AgentAdmin(admin.ModelAdmin):
    # fields 包含
    # exclude 排除
    # fields = ('secret_key',)
    # exclude = ('ctime',)
    pass


@admin.register(Config)
class ConfigAdmin(admin.ModelAdmin):
    pass


@admin.register(ServiceConfig)
class ServiceConfigAdmin(admin.ModelAdmin):
    pass


@admin.register(ConfigTemplate)
class ConfigTemplateAdmin(admin.ModelAdmin):
    pass


@admin.register(LogItem)
class LogItemAdmin(admin.ModelAdmin):
    pass


@admin.register(Operator)
class OperatorAdmin(admin.ModelAdmin):
    pass


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    pass


@admin.register(OperatorGroupRef)
class OperatorGroupRefAdmin(admin.ModelAdmin):
    pass


"""
@admin.register(Agent)
使用装饰器的方式,替代以下代码
"""
# admin.site.register(Agent, AgentAdmin)
# admin.site.register(Config, ConfigAdmin)
# admin.site.register(ServiceConfig, ServiceConfigAdmin)
# admin.site.register(ConfigTemplate, ConfigTemplateAdmin)
# admin.site.register(LogItem, LogItemAdmin)
# admin.site.register(Operator, OperatorAdmin)
# admin.site.register(Group, GroupAdmin)
# admin.site.register(OperatorGroupRef, OperatorGroupRefAdmin)
