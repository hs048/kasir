
from django.urls import path
from artikel.views import berita, berita_detil, sinkron_berita

urlpatterns = [
    
    path('', berita, name='berita'),
    path('sinkron-berita', sinkron_berita, name='sinkron_berita'),
    path('detil/<str:title>', berita_detil, name='berita_detil'),
   
]
