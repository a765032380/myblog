
from django.conf.urls import url

from blog import search
from . import views


urlpatterns = [
    url('^deletedb$', views.deletedb),
    url('^savedb$', views.savedb),
    url('^selectdb$', views.selectdb),
    url('^updatedb$', views.updatedb),

    url('^search-form$', search.search_form),
    url('^submit$', search.submit),
]
