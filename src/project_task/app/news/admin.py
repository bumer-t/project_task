from django.contrib import admin
from app.news.models import News, Comment

admin.site.register(News)
admin.site.register(Comment)
