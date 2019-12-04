
from django.conf.urls import url

from blog import search
from . import views


urlpatterns = [
    url('^delete$', search.delete),
    url('^savedb$', views.savedb),
    url('^selectdb$', views.selectdb),
    url('^update$', search.update),

    url('^select$', search.select),
    url('^add$', search.add),
    url('^update_view$', search.update_view),
    url('^registered', search.registered),

]
