from django.conf.urls import url

from blog import search, user_api,video_api
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

    # 测试爬虫
    url('^test_reptile',video_api.test_reptile)


]
