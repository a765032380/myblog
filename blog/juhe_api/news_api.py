from blog.models import News
from blog.utils import return_success, return_failure


def api_news(request):
    page = 0
    try:
        page = request.GET['page']
    except Exception as e:
        print(e)
    try:
        joke_list = News.objects.all().values()[int(page)*10:int(page)*10+10]
        return return_success(list(joke_list))
    except:
        return return_failure(code=2004,msg="没有更多数据")
