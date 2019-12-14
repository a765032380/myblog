

from django.http import HttpResponse
from django.shortcuts import render, redirect

from blog.models import User
from blog.utils import return_failure, return_success, object_to_json


def login(request):
    if request.POST:
        userName = request.POST['userName']
        passWord = request.POST['passWord']
        # book = User.objects.get(password=passWord, name=userName)

        try:
            book = User.objects.get(password=passWord, name=userName)
        except:
            return return_failure(code=2001,msg="验证码或密码不正确")

    return return_success(object_to_json(book))


def registered(request):
    if request.POST:
        userName = request.POST['userName']
        passWord = request.POST['passWord']
        # 判断用户名
        try:
            user = User.objects.get(name=userName)
        except Exception as e:
            user = None
        if user:
            return return_failure(code=2002, msg="当前用户已存在")
        # if any(book):
        #     return return_failure(code=2002, msg="当前用户已存在")
        # except:
        test1 = User(name=userName, password=passWord)
        test1.save()
        book = User.objects.get(pk=test1.pk)

    return return_success(object_to_json(book))

