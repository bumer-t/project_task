# -*- coding: utf-8 -*-
# Create your views here.
import simplejson
from django.template.loader import get_template #ищет и возвращает шаблон
from django.http import HttpResponse # основной НТТР ответ
from django.template import RequestContext # для передачи переменных в шаблон

#from portal.news.models import News, Comment # подключаем модели(таблицы бд0)
#from portal.news.forms import CommentForm # подключаем чт с формы
from django.http import HttpResponseRedirect #для переадресации
from django.core.urlresolvers import reverse
from django.contrib import auth #для работы с авторизацией-джанго
from django.template.response import TemplateResponse
from django.conf import settings
from django.contrib.auth.decorators import login_required

#для регистрации
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render_to_response
from django.template import RequestContext
#forma
from .forms import UploadFileForm
#
from .models import UploadFile


import shutil
#
import PIL, os
#from PIL import Image

def custom_proc(request):

    return
# {
#        'auth_form': AuthenticationForm(),
#        }

#тестовая вьюха
#def profile_show(request):
#    if request.user.is_authenticated():
#        user_name = request.user.username
#    else:
#        user_name = 'Гость'
#    template = get_template("profile.html")
#    context = RequestContext(request, {"user_name":user_name,})
#    return HttpResponse(template.render(context))

#def auth_show(request, template = 'index.html'):
#    if request.POST:
#        form = AuthenticationForm(request.POST)
#    context = {}
#    return render_to_response(template, context,
#                context_instance=RequestContext(request, processors=[custom_proc]))

#

def login(request, template='login_page.html'):
    context = {}
    return TemplateResponse(request, template, context)

@login_required
def upload_file(request, template='index.html'):
    rez = None
    if request.POST:
        form = UploadFileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
#            import ipdb; ipdb.set_trace()
            UploadFile(user=request.user, name=request.POST['name'], file=request.FILES['file']).save()
            return HttpResponseRedirect('/')
    else:
        form = UploadFileForm()

    if request.user.is_authenticated():
        rez = UploadFile.objects.filter(user=request.user)

    context = {'form':form, 'rez':rez}
    return render_to_response(template, context,
                context_instance=RequestContext(request)) #, processors=[custom_proc])

def file_list(request, template='files.html'):
    if request.user.is_authenticated():
        files = UploadFile.objects.filter(user=request.user)
    context = {
               'files': files,
              }
    return TemplateResponse(request, template, context)

def file_delete(request, file_id=0):
    try:
        file = UploadFile.objects.get(id=file_id)
    except:
        data = {"rezult":"error"}
    else:
        file.file.delete()
        file.delete()
        data = {"rezult":"OK"}

    return HttpResponse(simplejson.dumps(data))


#---------------
#регистрация
#def register(request):
#    if request.method == "POST":
#        form = UserCreationForm(request.POST)
#        if form.is_valid():
#            new_user = form.save()
#            return HttpResponseRedirect("/news/")
#    else:
#        form = UserCreationForm()
#    return render_to_response("register.html",{
#        'form':form,
#    })
#
#def login_view(request):
#    username = request.POST.get('username','')
#    password = request.POST.get('password','')
#    user = auth.authenticate(username=username, password=password)
#    if user is not None and user.is_active:
#        auth.login(request,user)
#        return HttpResonseRedirect("/account/loggedin")
#    else:
#        return HttpResponseRedirect("/account/invalid/")
#
##Функция ресайза изображения. Автоматически изменяет размер, сохраняя пропорции:
#def imageResize(data, output_size):
#   image = Image.open(data)
#   m_width = float(output_size[0])
#   m_height = float(output_size[1])
#   if image.mode not in ('L','RGB'):
#       image = image.convert('RGB')
#   w_k = image.size[0]/m_width
#   h_k = image.size[1]/m_height
#   if output_size < image.size:
#       if w_k > h_k:
#           new_size = (m_width, image.size[1]/w_k)
#       else:
#           new_size = (image.size[0]/h_k, m_height)
#
#   else:
#       new_size = image.size
#   return image.resize(new_size, Image.ANTIALIAS)

