from django.contrib import admin
from import_export.admin import ExportActionModelAdmin, ImportExportMixin, ImportMixin
from .models import ToiletInfo, Comment

# Register your models here.
class ToiletAdmin(ImportExportMixin,admin.ModelAdmin):
    pass
    ordering = ['id']
    list_display = ('id' , 'tname', 'tlocation', 'tlat', 'tlong')
    search_fields = ['tname']

class CommentAdmin(admin.ModelAdmin):
    search_fields = ('author', 'tname')

admin.site.register(ToiletInfo,ToiletAdmin)
admin.site.register(Comment, CommentAdmin)