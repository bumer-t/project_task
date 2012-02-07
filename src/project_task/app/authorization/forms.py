# -*- coding: utf-8 -*-
from django import forms
from django.forms.widgets import RadioSelect #, CheckboxSelectMultiple
from django.forms.fields import DateField, ChoiceField #, MultipleChoiceField
from django.forms.extras.widgets import SelectDateWidget
import datetime
from datetime import datetime, timedelta

from django.forms import ModelForm
from authorization.models import Profile

# форма для редактирование профиля юзера
GENDER_CHOICES = (('0', 'мужской'), ('1', 'женский'))
d = datetime.today()
BIRTH_YEAR_CHOICES = xrange(1950, int(d.strftime('%Y')) -5 )




#class EditProfileForm(forms.Form):
#    username = forms.CharField(label='Имя',required=True,widget=forms.TextInput(attrs={'size':'30','maxlength':'255'}))
#    birth_year = DateField(label='Дата рождения', widget=SelectDateWidget(years=BIRTH_YEAR_CHOICES))
#    gender = ChoiceField(label='Пол', widget=RadioSelect, choices=GENDER_CHOICES)
#    email = forms.EmailField(required=False, label='Ваш адрес e-mail') #neobyazatel'nnoe pole
#    town = forms.CharField(label='Город',required=True,widget=forms.TextInput(attrs={'size':'30','maxlength':'255'}))


class EditProfileForm(ModelForm):
    birth_year = DateField(label='Дата рождения', widget=SelectDateWidget(years=BIRTH_YEAR_CHOICES))
    sex = ChoiceField(label='Пол', widget=RadioSelect, choices=GENDER_CHOICES)
    class Meta:
        model = Profile
        exclude = ('user',)     # то что не выводить
    
    #http://www.askdev.ru/django/8213/Django-%D0%B7%D0%B0%D0%B3%D1%80%D1%83%D0%B7%D0%BA%D0%B0-%D0%B8%D0%B7%D0%BE%D0%B1%D1%80%D0%B0%D0%B6%D0%B5%D0%BD%D0%B8%D0%B9-%D0%B8-%D0%B8%D1%85-%D0%B2%D0%B0%D0%BB%D0%B8%D0%B4%D0%B0%D1%86%D0%B8%D1%8F/
  #  img = forms.    
    #captcha = CaptchaField(label='Enter symbols on image')
    
    
    
    #https://docs.djangoproject.com/en/dev/topics/forms/
    #https://docs.djangoproject.com/en/dev/ref/forms/widgets/
    #http://www.askdev.ru/django/8213/Django-%D0%B7%D0%B0%D0%B3%D1%80%D1%83%D0%B7%D0%BA%D0%B0-%D0%B8%D0%B7%D0%BE%D0%B1%D1%80%D0%B0%D0%B6%D0%B5%D0%BD%D0%B8%D0%B9-%D0%B8-%D0%B8%D1%85-%D0%B2%D0%B0%D0%BB%D0%B8%D0%B4%D0%B0%D1%86%D0%B8%D1%8F/
    #http://groups.google.com/group/django-russian/browse_thread/thread/9eab86984140bf96