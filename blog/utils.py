import json

from django.http import HttpResponse

from blog.header import Header


def object_to_json(obj):
    return dict([(kk, obj.__dict__[kk]) for kk in obj.__dict__.keys() if kk != "_state"])


def return_success(data):
    res = {'code': 200, 'msg': "成功", 'data': data}
    return HttpResponse(str(res).replace("'", '"'))


def return_failure(code, msg, data_bean=""):
    res = {'code': code, 'msg': msg, 'data': data_bean}
    return HttpResponse(str(res).replace("'", '"'))


def get_header(request):
    header = Header(request.META.get("HTTP_ID", 'un_know'),
                    request.META.get("HTTP_PLATFORM", 'un_know'),
                    request.META.get("HTTP_SYSVERSION", 'un_know'),
                    request.META.get("HTTP_DEVICE", 'un_know'),
                    request.META.get("HTTP_SCREEN", 'un_know'),
                    request.META.get("HTTP_UUID", 'un_know'),
                    request.META.get("HTTP_VERSION", 'un_know'),
                    request.META.get("HTTP_APIVERSION", 'un_know'),
                    request.META.get("HTTP_TOKEN", 'un_know'),
                    request.META.get("HTTP_CHANNELID", 'un_know'),
                    request.META.get("HTTP_NETWORKTYPE", 'un_know'))
    print('\n'.join(['%s:%s' % item for item in header.__dict__.items()]))
    return header

