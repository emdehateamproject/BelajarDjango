from django.contrib import admin
from .models import pegawai
from .models import dokumen
# Register your models here.


# admin.site.register(dokumen)
@admin.register(pegawai)
class pegawaiAdmin(admin.ModelAdmin):
    list_display = ['nama','alamat','jenis_kelamin','golongan']

@admin.register(dokumen)
class dokumenAdmin(admin.ModelAdmin):
    list_display = ['no','name','activity','quantity','date','img_file']