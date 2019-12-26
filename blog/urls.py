from django.conf.urls import url

from blog import search, user_api,video_api
from blog.juhe_api import joke, joke_api, news_api
from . import views

urlpatterns = [
    url('^delete$', search.delete),
    url('^savedb$', views.savedb),
    url('^selectdb$', views.selectdb),
    url('^update$', search.update),

    url('^select$', search.select),
    url('^add$', search.add),
    url('^update_view$', search.update_view),
    url('^home', views.selectdb),

    # api相关的
    # user_api
    url('^registered', user_api.registered),
    url('^login', user_api.login),

    # video_api
    url('^select_video',video_api.select_video),

    # 笑话API
    url('^api_joke', joke_api.api_joke),

    # 新闻API
    url('^api_joke', news_api.api_news),
    # 测试爬虫
    url('^test_reptile',video_api.test_reptile)




]
