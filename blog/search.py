# -*- coding: utf-8 -*-
import json

from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import  render, redirect

# 表单
from blog.models import Test, User


def select(request):
    data = {}
    # data['code'] = 200
    # data['msg'] = "成功"
    test = Test.objects.values()
    data['data'] = list(test)
    return render(request, "formdb.html", data)


def update_view(request):
    ctx = {}
    if request.POST:
        ctx['title'] = request.POST['title']
        ctx['context'] = request.POST['context']
        ctx['id'] = request.POST['id']

    return render(request, "formdb_update.html", ctx)


# 接收请求数据
def add(request):
    ctx = {}
    if request.POST:
        ctx['rlt'] = request.POST['title']
        ctx['rlc'] = request.POST['context']

        test1 = Test(title=request.POST['title'], context=request.POST['context'])
        test1.save()
    return redirect('/blog/select')


def delete(request):
    # 删除id=1的数据
    if request.POST:
        print("id=" + request.POST['id'])
        test1 = Test.objects.get(id=request.POST['id'])
        test1.delete()

    # 另外一种方式
    # Test.objects.filter(id=1).delete()

    # 删除所有数据
    # Test.objects.all().delete()

    return redirect('/blog/select')


def update(request):
    # 修改其中一个id=1的name字段，再save，相当于SQL中的UPDATE
    if request.POST:
        print("id=" + request.POST['id'])
        test1 = Test.objects.get(id=request.POST['id'])
        test1.context = request.POST['context']
        test1.title = request.POST['title']
        test1.save()
    # 另外一种方式
    # Test.objects.filter(id=1).update(name='Google')

    # 修改所有的列
    # Test.objects.all().update(name='Google')

    return redirect('/blog/select')


def login(request):
    if request.POST:
        userName = request.POST['userName']
        passWord = request.POST['passWord']
        # book = User.objects.get(password=passWord, name=userName)

        try:
            book = User.objects.get(password=passWord, name=userName)
        except:
            res = {'code': 2001, 'msg': "验证码或密码不正确"}
            return return_http(request,res)

        res = {'code': 200, 'msg': "成功", 'data': object_to_json(book)}
    return return_http(request,res)


def registered(request):
    if request.POST:
        userName = request.POST['userName']
        passWord = request.POST['passWord']
        test1 = User(name=userName, password=passWord)
        test1.save()

        res = {'code': 200, 'msg': "成功"}
        book = User.objects.get(pk=test1.pk)
        res['data'] = object_to_json(book)
    return return_http(request,res)


def object_to_json(obj):
    return dict([(kk, obj.__dict__[kk]) for kk in obj.__dict__.keys() if kk != "_state"])


def return_http(request,res):
    return HttpResponse(request,str(res).replace("'", '"'), content_type="application/json;charset=utf-8")
