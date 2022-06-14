from django.contrib import admin
from .models import Talaba,Yonal
from import_export.admin import ExportActionMixin
class TalabaAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display=('id','familiya','ism','ota_ism','phone','talim','yonal','diplom','pasport','pasport_image_tag','diplom_image_tag','image_3x4_tag','added_date')

admin.site.register(Talaba,TalabaAdmin)
admin.site.register(Yonal)
