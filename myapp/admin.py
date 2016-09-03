from django.contrib import admin
from django.contrib.admin import AdminSite
from models import Post


# class KidsrpAdminSite(AdminSite):
AdminSite.site_header = 'Nazokake admin'
AdminSite.site_title = 'Nazokake admin'
admin.ModelAdmin.list_per_page = 20


# class MyAdmin(admin.ModelAdmin):
#   class Media:
#     css = {
#       'all': ('css/my_styles.css',)
#     }
#   def logo_tag(self, obj):
#     return u'<img src="/media/%s" width="100" />' % obj.logo
#   logo_tag.short_description = 'Image'
#   logo_tag.allow_tags = True

#   def image_tag(self, obj):
#     return u'<img src="/media/%s" width="100" />' % obj.image
#   image_tag.short_description = 'Image'
#   image_tag.allow_tags = True

#   def avatar_tag(self, obj):
#     return u'<img src="/media/%s" width="100" />' % obj.avatar
#   avatar_tag.short_description = 'Avatar'
#   avatar_tag.allow_tags = True

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'kakeru', 'toku', 'kokoro')
    pass
