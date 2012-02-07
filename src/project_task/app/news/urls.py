# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *
#
urlpatterns = patterns('news.views',
    url(r'^$','last_news',name = 'news.last_news'),
    url(r'^(?P<news_id>\d+)/$','news_detail',name = 'news.news_detail'),) # тема стала ссылкой и так работает тут через заглушку
