#-*-coding:utf-8 -*-
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "P_QQ_Management.settings")
import django
django.setup()

from QQUser.models import QQUser
import xlrd

def import_qq_excel():
    try:
        # 数据源：test-file.xls
        data = xlrd.open_workbook("test-file.xls")
        # 第一章工作表
        table = data.sheets()[0]
        nrows = table.nrows
        print("开始将QQ信息导入数据库！")
        for i in range(1, nrows):
            item = table.row_values(i)
            # QQ号：位于工作表第1列
            QQ = str(int(item[0]))
            print(QQ)
            # 昵称：位于工作表第2列
            NickName = item[1]
            # 用户类别：：位于工作表第3列
            UserType = item[2]
            # 创建QQUser对象
            qqUser = QQUser(QQ = QQ, NickName = NickName, UserType = UserType)
            # 将QQUser对象保存到数据库中
            qqUser.save()
        print("QQ信息导入成功")
    except Exception as e:
        print(str(e))

if __name__ == '__main__':
    import_qq_excel()