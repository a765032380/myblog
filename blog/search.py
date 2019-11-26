# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import render_to_response, render

# 表单
from blog.models import Test


def search_form(request):
    return render_to_response('formdb.html')


# 接收请求数据
def submit(request):
    ctx = {}
    if request.POST:
        ctx['rlt'] = request.POST['title']
        ctx['rlc'] = request.POST['context']

        test1 = Test(title=request.POST['title'], context=request.POST['context'])
        test1.save()
        message = '你提交的title=' + request.POST['title']+'-----你提交的context='+request.POST['context']

    return render(request, "formdb.html", ctx)
