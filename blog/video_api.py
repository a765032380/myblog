# -*- coding:UTF-8 -*-

import json
import re
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
    target = 'http://www.biqukan.com/1_1094/5403177.html'
    req = requests.get(url=target)
    html = req.text
    bf = BeautifulSoup(html)
    texts = bf.find_all('div', class_='showtxt')
    print(texts[0].text.replace('\xa0' * 8, '\n\n'))

    return return_success("")


