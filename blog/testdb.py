# -*- coding: utf-8 -*-
from django.http import HttpResponse, JsonResponse

# 数据库操作
from blog.models import Test
import json
from django.core import serializers

# 数据库操作
def savedb(request):
    for num in range(1, 20):
        test1 = Test(title='我是标题'+str(num), context='我是内容'+str(num))
        test1.save()
    return HttpResponse("<p>数据添加成功！</p>")

def selectdb(request):
    # 初始化
    data = {}
    data['code'] = 200
    data['msg'] = "成功"
    book = Test.objects.values()
    data['data'] = list(book)
    return HttpResponse("<p>" + str(data).replace("'", '"') + "</p>")


# 数据库操作
def updatedb(request):
    # 修改其中一个id=1的name字段，再save，相当于SQL中的UPDATE
    test1 = Test.objects.get(title='')
    test1.title = 'Google'
    test1.save()

    # 另外一种方式
    # Test.objects.filter(id=1).update(name='Google')

    # 修改所有的列
    # Test.objects.all().update(name='Google')

    return HttpResponse("<p>修改成功</p>")


# 数据库操作
def deletedb(request):
    # 删除id=1的数据
    # test1 = Test.objects.get(id=1)
    # test1.delete()

    # 另外一种方式
    # Test.objects.filter(id=1).delete()

    # 删除所有数据
    Test.objects.all().delete()

    return HttpResponse("<p>删除成功</p>")