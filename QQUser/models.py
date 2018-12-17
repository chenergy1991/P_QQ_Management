# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
USER_TYPE_CHOICE = (
    ('黑名单', '黑名单'),
    ('白名单', '白名单'),
    ('未归档', '未归档'),
)

class QQUser(models.Model):
    QQ = models.CharField("QQ号", max_length=15)
    NickName = models.CharField("QQ昵称", max_length=30)
    UserType = models.CharField("用户类型", choices=USER_TYPE_CHOICE, default=USER_TYPE_CHOICE[2], max_length=50)

    class Meta:
        verbose_name = u'QQ管理表'
        verbose_name_plural = u"QQ管理表"