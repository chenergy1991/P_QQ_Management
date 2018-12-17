# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import QQUser
# 导入函数export_as_csv_action
from QQUser.csvutil import export_as_csv_action


class QQUserExcelToolAdmin(admin.ModelAdmin):
    list_display = ('QQ','NickName','UserType')
    search_fields = ('QQ','NickName','UserType')
    # 添加函数export_as_csv_action，自定义action
    actions = [export_as_csv_action('导出表格',fields=['QQ', 'NickName', 'UserType'])]
# 注册后台显示相应model信息：
admin.site.register(QQUser, QQUserExcelToolAdmin)