# -*- coding: utf-8 -*-
from django.db import models
from django.db.models import signals
from django.contrib.auth.models import User
from django.conf import settings

import PIL, os
from PIL import Image

from django.db.models import signals

from django.utils.translation import ugettext_lazy as _


# Create your models here.

#class AvatarImageField(models.ImageField):
#    def save_form_data(self, instance, data):
#        from StringIO import StringIO
#        from django.core.files.uploadedfile import SimpleUploadedFile, UploadedFile
#
#        if data and isinstance(data, UploadedFile):
#            image = imageResize(data, settings.AVATAR_SIZE)
#            new_imaged = StringIO()
#            image.save(new_image, 'JPEG', quality=85)
#            data = SimpleUploadedFile(data.name, new_image.getvalue(), data.content_type)
#
#            # Удаление старого файла
#            previous = u'%s%s' % (settings.MEDIA_ROOT, instance.avatar)
#            if os.path.isfile(previous):
#                os.remove(previous)
#      # -
#        super(AvatarImageField, self).save_form_data(instance, data)
#    
#def make_upload_path(instance, filename, prefix = False):
#    # Переопределение имени загружаемого файла.
#    from utils.hashfunc import get_hash
#    filename = 'a_' + get_hash('md5') + '.jpg'
#    import ipdb; ipdb.set_trace()
#    return u"%s/%s" % (settings.AVATAR_UPLOAD_DIR, filename)

#def create_profile_for_user(sender, instance, signal, **kwargs):
#            try:
##                import ipdb; ipdb.set_trace()
#                Profile.objects.get(user=instance)
#            except (Profile.DoesNotExist, AssertionError):
#                    p = Profile(user=instance)
#                    p.save()
#
#signals.post_save.connect(create_profile_for_user, sender=User)


class UploadFile(models.Model):
    user = models.ForeignKey(User) #related_name=''
    name = models.CharField(max_length=20)
    date = models.DateTimeField(auto_now_add=True)
    file = models.FileField(_(u'File'), upload_to='files')

    
    class Admin:
        pass
    
    def __unicode__(self):
        return self.name
