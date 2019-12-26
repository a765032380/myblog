#!/usr/bin/python
# -*- coding: utf-8 -*-
import json, urllib
import time
from collections import namedtuple
from urllib import request


# ----------------------------------
# 笑话大全调用示例代码 － 聚合数据
# 在线接口文档：http://www.juhe.cn/docs/95
# ----------------------------------
from urllib.parse import urlencode


from blog.models import Joke
from blog.utils import object_to_json


def main():
    # 配置您申请的APPKey
    appkey = "1064f77cfe93ee5d2b808a21036152c9"

    # 1.按更新时间查询笑话
    # request1(appkey, "GET")

    # # 2.最新笑话
    request1(appkey, "GET")
    #
    # # 3.按更新时间查询趣图
    # request3(appkey, "GET")
    #
    # # 4.最新趣图
    # request4(appkey, "GET")


# 按更新时间查询笑话
def request1(appkey, m="GET"):
    url = "http://japi.juhe.cn/joke/content/list.from"
    params = {
        "sort": "",  # 类型，desc:指定时间之前发布的，asc:指定时间之后发布的
        "page": "",  # 当前页数,默认1
        "pagesize": "",  # 每次返回条数,默认1,最大20
        "time": (int(time.time())),  # 时间戳（10位），如：1418816972
        "key": appkey,  # 您申请的key

    }
    params = urlencode(params)
    if m == "GET":
        f = request.urlopen("%s?%s" % (url, params))
    else:
        f = request.urlopen(url, params)

    content = f.read().decode()
    res = json.loads(content)
    print_res(res)


# 最新笑话
def request2(appkey, m="GET"):
    url = "http://japi.juhe.cn/joke/content/text.from"
    params = {
        "page": "",  # 当前页数,默认1
        "pagesize": "",  # 每次返回条数,默认1,最大20
        "key": appkey,  # 您申请的key

    }
    params = urlencode(params)
    if m == "GET":
        f = request.urlopen("%s?%s" % (url, params))
    else:
        f = request.urlopen(url, params)

    content = f.read()
    res = json.loads(content)
    print_res(res)


# 按更新时间查询趣图
def request3(appkey, m="GET"):
    url = "http://japi.juhe.cn/joke/img/list.from"
    params = {
        "sort": "",  # 类型，desc:指定时间之前发布的，asc:指定时间之后发布的
        "page": "",  # 当前页数,默认1
        "pagesize": "",  # 每次返回条数,默认1,最大20
        "time":(int(time.time())),  # 时间戳（10位），如：1418816972
        "key": appkey,  # 您申请的key

    }
    params = urlencode(params)
    if m == "GET":
        f = request.urlopen("%s?%s" % (url, params))
    else:
        f = request.urlopen(url, params)

    content = f.read()
    res = json.loads(content)
    print_res(res)


# 最新趣图
def request4(appkey, m="GET"):
    url = "http://japi.juhe.cn/joke/img/text.from"
    params = {
        "page": "",  # 当前页数,默认1
        "pagesize": "",  # 每次返回条数,默认1,最大20
        "key": appkey,  # 您申请的key

    }
    params = urlencode(params)
    if m == "GET":
        f = request.urlopen("%s?%s" % (url, params))
    else:
        f = request.urlopen(url, params)

    content = f.read()
    res = json.loads(content)
    print_res(res)


def print_res(res):
    if res:
        error_code = res["error_code"]
        if error_code == 0:
            # 成功请求
            json_str = res["result"]["data"]
            # joke_list = json.loads(json_str, object_hook=lambda d: namedtuple('data', d.keys()))
            joke_list = json.loads(str(json_str).replace("'", '"'))
            # joke_list = demjson.decode(str(json_str).replace("'", '"'))
            for joke in list(joke_list):
                try:
                    user = Joke.objects.get(hashId=get_res(joke, 'hashId'))
                except Exception as e:
                    user = None
                if user:
                    print('本条笑话数据已存在')
                else:
                    j = Joke()
                    j.content = get_res(joke, 'content')
                    j.hashId = get_res(joke, 'hashId')
                    j.unixTime = get_res(joke, 'unixtime')
                    j.updateTime = get_res(joke, 'updatetime')
                    j.url = get_res(joke, 'url')
                    j.save()
        else:
            print("%s:%s" % (res["error_code"], res["reason"]))
    else:
        print("request api error")


def get_res(joke,values):
    try:
        return joke[values]
    except Exception as e:
        return ''




if __name__ == '__main__':
    main()
    # print_res("")