# -*- coding: utf-8 -*-
from django import forms
# форма для комментов
class CommentForm(forms.Form):
    #username = forms.CharField(label="Имя",required=True, min_length=2, max_length=50)
    #text = forms.CharField(label="Текст",widget=forms.Textarea)
    username = forms.CharField(label='Имя',required=True,widget=forms.TextInput(attrs={'size':'30','maxlength':'255'}))
    text = forms.CharField(label="Текст", required=True, widget=forms.Textarea())    
    #captcha = CaptchaField(label='Enter symbols on image')