from django.urls import path ,include
from .views import *

urlpatterns = [
    path('',dashboard, name='dashboard'),
    path('blog',blog, name='table_blog'),
    path('doa',doa, name='tabel_doa'),
    path('sholat',sholat, name='tabel_sholat'),
    path('users/',users, name='table_users'),
    path('sinkron_doa/',sinkron_doa, name='sinkron_doa'),
    path('sinkron_sholat/',sinkron_sholat, name='sinkron_sholat'),
    path('blog/tambah',tambah_blog, name='tambah_blog'),
    path('blog/lihat/<str:id>',lihat_blog, name='lihat_blog'),
    path('blog/edit/<str:id>',edit_blog, name='edit_blog'),
    path('blog/delete/<str:id>',delete_blog, name='delete_blog'),
]