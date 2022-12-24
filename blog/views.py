from django.shortcuts import render,redirect
from multiprocessing import context
from .models import Artikel,Kategori,Sholat,Doa
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, user_passes_test
import requests

# def is_creator(user):
#     if user.groups.filter(name='Creator').exists():
#         return True
#     else:
#         return False

# @login_required
def dashboard(request):
    if request.user.groups.filter(name='Creator').exists():
        request.session['is_creator'] = 'creator'
    
    template_name = "back/dashboard.html"
    context = {
        'title' : 'dashboard',
    } 
    return render(request, template_name, context)

# @login_required
def blog(request):
    template_name = "back/tabel_blog.html"
    blog = Artikel.objects.all()
    print(blog)
    context = {
        'title' : 'dashboard',
        'blog': blog,
    }
    return render(request, template_name, context)
def doa(request):
    template_name = "back/tabel_doa.html"
    doa = Doa.objects.all()
    context = {
        'title' : 'dashboard',
        'doa': doa,
    }
    return render(request, template_name, context)
def sholat(request):
    template_name = "back/tabel_shalat.html"
    sholat = Sholat.objects.all()
    context = {
        'title' : 'dashboard',
        'sholat': sholat,
    }
    return render(request, template_name, context)


# @login_required
# @user_passes_test(is_creator)
def users(request):
    template_name = "back/tabel_users.html"
    list_user = User.objects.all()
    context = {
        'title' : 'dashboard',
        'list_user' : list_user
    }
    return render(request, template_name, context)

# @login_required
def tambah_blog(request):
    template_name = "back/tambah_blog.html"
    kategori = Kategori.objects.all()
    if request.method == "POST":
        kategori = request.POST.get('kategori')
        nama = request.POST.get('nama')
        judul = request.POST.get('judul')
        body = request.POST.get('body')
        kat = Kategori.objects.get(nama=kategori)
      
        #simpan produk karena ada relasi ke tabel kategori 
        Artikel.objects.create(
            nama = nama,
            judul = judul,
            body = body,
            kategori = kat,
        )
        return redirect (blog)
    context = {
        'title':'Tambah Blog',
        'kategori':kategori,

    }
    return render(request, template_name, context)

# @login_required
def lihat_blog(request, id):
    template_name = "back/lihat_blog.html"
    blog = Artikel.objects.get(id=id)
    context = {
        'title' : 'View Blog',
        'blog' :blog,
    }
    return render(request, template_name, context)

# @login_required
def edit_blog(request ,id ):
    template_name = 'back/edit_blog.html'
    kategori = Kategori.objects.all()
    a = Artikel.objects.get(id=id)
    if request.method == "POST":
        
        kategori = request.POST.get('kategori')
        nama = request.POST.get('nama')
        judul = request.POST.get('judul')
        body = request.POST.get('body')
        kat = Kategori.objects.get(nama=kategori)

        #input Kategori Dulu
        

        #simpan produk karena ada relasi ke tabel kategori 
        a.nama = nama
        a.judul = judul
        a.body = body
        a.kategori = kat
        a.save() 
        return redirect(blog)
    context = {
        'title':'Edit Blog',
        'kategori':kategori,
        'blog' : blog,

    }
    return render(request, template_name, context)

# @login_required
def delete_blog(request,id):
    Artikel.objects.get(id=id).delete()
    return redirect(blog)

def sinkron_sholat(request):
	url = "https://cdn.statically.io/gh/lakuapik/jadwalsholatorg/master/adzan/samarinda/2022/12.json"
	data = requests.get(url).json()
	for d in data:
		cek_berita = Sholat.objects.filter(tanggal=d['tanggal'])
		if cek_berita:
			print('data sudah ada')
			c = cek_berita.first()
			c.tanggal=d['tanggal']
			c.save()
		else: 
      		#jika belum ada maka tulis baru kedatabase
			b = Sholat.objects.create(
				tanggal = d['tanggal'],
				imsyak = d['imsyak'],
				shubuh = d['shubuh'],
				terbit = d['terbit'],
				dhuha = d['dhuha'],
				dhuhur = d['dzuhur'],
				ashr = d['ashr'],
				magrib = d['magrib'],
				isya = d['isya'],
			)
	return redirect(sholat)
def sinkron_doa(request):
        url = "https://doa-doa-api-ahmadramadhan.fly.dev/api"
        data = requests.get(url).json()
        for d in data:
            cek_berita = Doa.objects.filter(id=d['id'])
            if cek_berita:
                print('data sudah ada')
                c = cek_berita.first()
                c.id=d['id']
                c.save()
            else: 
                #jika belum ada maka tulis baru kedatabase
                b = Doa.objects.create(
                    id = d['id'],
                    doa = d['doa'],
                    ayat = d['ayat'],
                    latin = d['latin'],
                    artinya = d['artinya'],
                )
        return redirect(doa)