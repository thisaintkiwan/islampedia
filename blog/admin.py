from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Kategori)



class ArtikelAdmin(admin.ModelAdmin):
    list_display = ('nama','judul','body','kategori','date')
admin.site.register(Artikel, ArtikelAdmin)

class DoaAdmin(admin.ModelAdmin):
    list_display = ('id','doa','ayat','latin','artinya')
admin.site.register(Doa, DoaAdmin)

class ShalatAdmin(admin.ModelAdmin):
    list_display = ('tanggal','imsyak','shubuh','terbit','dhuha','dhuhur','ashr','magrib','isya')
admin.site.register(Sholat, ShalatAdmin)

