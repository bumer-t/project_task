# -*- coding: utf-8 -*-
# Create your views here.

from datetime import datetime
from django.template.loader import get_template #ищет и возвращает шаблон
from django.http import HttpResponse # основной НТТР ответ
from django.template import RequestContext # для передачи переменных в шаблон

from app.news.models import News, Comment # подключаем модели(таблицы бд0)
from app.news.forms import CommentForm # подключаем чт с формы
from django.http import HttpResponseRedirect #для переадресации
from django.core.urlresolvers import reverse

from django.shortcuts import get_object_or_404
from django.http import Http404
from django.shortcuts import render_to_response
from app.authorization.views import custom_proc

def last_news(request):
    news = News.objects.filter(pub_date__lte=datetime.now()).order_by("-pub_date")[:10]
    template = get_template("last_news.html")
    context = RequestContext(request, {"last_news":news,})
    return HttpResponse(template.render(context))

#представление-заглушку для нового типа URL. В новостях тема - стала ссылкой
def news_detail(request, news_id):
    news = News.objects.get(pk=news_id) #выбираем 1 объект, где pk=id
    if request.method == 'POST': # если дА-то форма была отправлена юзером. Если нет то был -GET
        form = CommentForm(request.POST)
        if form.is_valid():  #правильна ли заполнена форма
            comment = Comment(
                news = news,
                username = form.cleaned_data['username'], #конвертируета данные в подходящий тип питона
                text = form.cleaned_data['text']
            )
            comment.save() #сохраняем объект в бд
            return HttpResponseRedirect(
                reverse('news.news_detail',kwargs={'news_id':news_id}))
            # переадресовываем на станицу с параметром id 
    else:
        #form = CommentForm()
        form = CommentForm(initial={'username':request.user.username})
        print "с формы передача не идёт :( "
    
    comments = Comment.objects.filter(news=news).order_by("-pub_date","id")
    comment_count = comments.count()
    template = "news_detail.html"
    context = {
            "news":news,
            "form":form,
            "comment_count":comment_count,
            "comments":comments}



    return render_to_response(template, context,
                    context_instance=RequestContext(request, processors=[custom_proc]))
    
    
    
    
    


