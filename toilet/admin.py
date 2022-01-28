from django.contrib import admin
from import_export.admin import ExportActionModelAdmin, ImportExportMixin, ImportMixin
from .models import ToiletInfo

# Register your models here.
class ToiletAdmin(ImportExportMixin,admin.ModelAdmin):
    pass


admin.site.register(ToiletInfo,ToiletAdmin)