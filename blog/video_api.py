import json

import requests
from bs4 import BeautifulSoup
from django.core import serializers
from django.http import JsonResponse

from blog.models import Video
from blog.utils import return_success, object_to_json, get_header


def select_video(request):
    header = get_header(request)
    video_list = Video.objects.order_by('?')[:10].values()
    return return_success(list(video_list))


def select_video_list(request):

    pass


def test_reptile(request):
    global result
    url = 'http://www.cntour.cn'
    str_html = requests.get(url)  # Get方式获取网页数据
    soup = BeautifulSoup(str_html.text, 'lxml')
    data = soup.select(
        '#main > div > div.mtop.firstMod.clearfix > div.leftBox > div:nth-child(2) > ul > li > a')
    for item in data:
        result = {
            'title': item.get_text(),
            'link': item.get('href')
        }
        print(result)
    return return_success("")


