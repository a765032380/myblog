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
    url('^get_joke', joke_api.get_joke),
    url('^add_joke', joke_api.add_joke_api),

    # 新闻API
    url('^get_joke', news_api.get_news),
    url('^add_joke', news_api.add_news_api),
    # 测试爬虫
    url('^test_reptile',video_api.test_reptile)




]
