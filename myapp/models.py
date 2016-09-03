from __future__ import unicode_literals

from django.db import models



class Post(models.Model):
    kakeru = models.CharField(max_length=128)
    toku = models.CharField(max_length=128)
    kokoro = models.CharField(max_length=128)
    like = models.IntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __unicode__(self):
        return u'%s' % self.kokoro


