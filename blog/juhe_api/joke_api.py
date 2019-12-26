from django.core.paginator import Paginator

from blog.models import Joke
from blog.utils import get_header, return_failure, return_success, object_to_json


def api_joke(request):
    page = 0
    try:
        page = request.GET['page']
    except Exception as e:
        print(e)
    try:
        joke_list = Joke.objects.all().values()[int(page)*10:int(page)*10+10]
        return return_success(list(joke_list))
    except:
        return return_failure(code=2004,msg="没有更多数据")

