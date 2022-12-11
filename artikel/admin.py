from django.contrib import admin
from artikel.models import Berita
# Register your models here.

class BeritaAdmin(admin.ModelAdmin):
    list_display = ['title','author','time']
    
admin.site.register(Berita, BeritaAdmin)
