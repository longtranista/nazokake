# -*- coding: utf-8 -*-
from rest_framework import serializers
from models import Post
from django.utils.http import urlencode, urlquote

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post

    # share_text = serializers.Field(source='share_text')
    share_text = serializers.SerializerMethodField()
    def get_share_text(self, obj):
      text = u'%s　とかけて　%s　と解きます。\nどちらも%s！　#なぞかけ   \n-  %s' % (obj.kakeru, obj.toku, obj.kokoro, 'http://nazokake.xyz')
      return urlquote(text)