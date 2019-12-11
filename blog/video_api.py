import json

from django.core import serializers
from django.http import JsonResponse

from blog.models import Video
from blog.utils import return_success, object_to_json, get_header


def select_video(request):
    header = get_header(request)
    print("ssssssssssssss")
    video_list = Video.objects.order_by('?')[:10].values()
    return return_success(list(video_list))
