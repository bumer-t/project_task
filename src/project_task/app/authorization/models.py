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

def create_profile_for_user(sender, instance, signal, **kwargs):
            try:
#                import ipdb; ipdb.set_trace()
                Profile.objects.get(user=instance)
            except (Profile.DoesNotExist, AssertionError):
                    p = Profile(user=instance)
                    p.save()

signals.post_save.connect(create_profile_for_user, sender=User)


class Profile(models.Model):
    #user_id = models.ForeignKey(User)
    user = models.ForeignKey(User, unique=True, related_name='profile')
    name = models.CharField(max_length=20, blank=True, null=True)
    birth_year = models.DateTimeField('дата', blank=True, null=True)
    sex = models.IntegerField(blank=True, null=True)
    sity = models.CharField(max_length=40, blank=True, null=True)
    email = models.EmailField(verbose_name='e-mail', unique=True, blank=True, null=True)
    image_profile = models.ImageField(_(u'Ава'), upload_to='images/profiles', blank=True, null=True)
 #   img = models.CharField(max_length=40)
#    avatar = AvatarImageField(
#        upload_to=make_upload_path,
#        null = False,
#        blank = False,
#        )
    
    class Admin:
        pass
    
    def __unicode__(self):
        return self.name
    
    
def resize_image_story(sender, instance, **kwargs):
    if instance.image_profile.name:
        image = Image.open(settings.PROJECT_ROOT+instance.image_profile.url)
        old_w = new_w = image.size[0]
        old_h = new_h = image.size[1]
        if old_w>300:
            new_w = 300
            new_h = new_w*old_h/old_w
        elif old_h>300: 
            new_h = 300
            new_w = old_w*new_h/old_h
        new_size = (new_w, new_h)
        image.thumbnail(new_size, Image.ANTIALIAS)
        image.save(settings.PROJECT_ROOT+instance.image_profile.url, "JPEG", quality=85)

signals.post_save.connect(resize_image_story, sender=Profile)