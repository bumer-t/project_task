# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, include, url
from django.contrib.auth.views import login, logout #авотризация
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from registration.forms import RegistrationFormUniqueEmail
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'portal.views.home', name='home'),
    # url(r'^portal/', include('portal.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
#     (r'^news/', include('news.urls')),   #при переходе к news/ будут подгружаться URL-карты, относящиеся к приложению.
#     (r'^profile/', include('authorization.urls')),
#     url(r'^register/$', 'registration.views.register',{'form': RegistrationFormUniqueEmail}, name='registration_register'),
#     (r'^accounts/', include('registration.urls')),
#     url(r'^$', 'authorization.views.auth_show'),
    url(r'', include('social_auth.urls')),
    url(r'^account/logout/$', logout, {'next_page': '/'}, name="logout"),
)

urlpatterns += patterns('project_task.views',
      url(r'^$', 'upload_file', name='index'),
      url(r'^login/$', 'login', name='login'),
      url(r'^files/$', 'file_list', name='files_url'),
      url(r'^file_del/(?P<file_id>\d+)', 'file_delete', name='file_delete_url'),
#      url(r'^del_file/(?P<file_id>\d+)', 'del_file'   , name="del_file"),
)

# for serving MEDIA files
if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
#        url(r'^files/(?P<path>.*)$', 'django.views.static.serve', {
#            'document_root': settings.MEDIA_ROOT+'/files',
#        }),

   )

urlpatterns += staticfiles_urlpatterns()
