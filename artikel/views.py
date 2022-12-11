import requests
from django.shortcuts import render, redirect
from artikel.models import Berita
# Create your views here.

def berita(request):
    template_name = "berita.html"
    get_berita = Berita.objects.all()
    context = {
		'berita' : get_berita
	}
    return render(request, template_name, context)


def berita_detil(request, title):
    template_name = "berita_detil.html"
    get_berita = Berita.objects.get(title=title)
    context = {
		'berita' : get_berita
	}
    return render(request, template_name, context)

def sinkron_berita(request):
	url = "https://the-lazy-media-api.vercel.app/api/games"
	data = requests.get(url).json()
	for d in data:
		cek_berita = Berita.objects.filter(title=d['title'])
		if cek_berita:
			print('data sudah ada')
			c = cek_berita.first()
			c.title=d['title']
			c.save()
		else: 
      		#jika belum ada maka tulis baru kedatabase
			b = Berita.objects.create(
				title = d['title'],
				thumb = d['thumb'],
				author = d['author'],
				tag = d['tag'],
				time = d['time'],
				desc = d['desc'],
				key = d['key']
			)
	return redirect(berita)



