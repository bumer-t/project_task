# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *
#
urlpatterns = patterns('authorization.views',
    url(r'^$','profile_show',name = 'authorization.profile_show'),
    url(r'^profile/edit$','profile_edit',name = 'authorization.profile_edit'),
    url(r'^edit$','profile_edit',name = 'authorization.profile_edit'),
    url(r'^register$','register',name = 'authorization.register'),
)
    #url(r'^(?P<news_id>\d+)/$','news_detail',name = 'news.news_detail'),) # тема стала ссылкой и так работает тут через заглушку
