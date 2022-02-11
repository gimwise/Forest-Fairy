from django.contrib import admin
from import_export.admin import ExportActionModelAdmin, ImportExportMixin, ImportMixin
from .models import ToiletInfo, Comment, Bookmarks
# Register your models here.
class ToiletAdmin(ImportExportMixin,admin.ModelAdmin):
    pass
    ordering = ['id']
    list_display = ('id' , 'tname', 'tlocation', 'tlat', 'tlong')
    search_fields = ['tname']

class CommentAdmin(admin.ModelAdmin):
    list_display = ('get_tname', 'score', 'author')
    search_fields = ['author']

    def get_tname(self, obj):
        return obj.toilet.tname

class BookMarkAdmin(admin.ModelAdmin):
    list_display = (
        'get_tname',
        'user'
    )
    def get_tname(self, obj):
        return obj.toilet.tname

admin.site.register(ToiletInfo,ToiletAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Bookmarks, BookMarkAdmin)