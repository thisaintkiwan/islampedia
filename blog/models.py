from tabnanny import verbose
from unittest.util import _MAX_LENGTH
from django.db import models

from django.contrib.auth.models import User
from django.db.models.fields.related import ForeignKey
# Create your models here.
class Kategori(models.Model):
    nama = models.CharField(max_length=100)
    
    def __str__(self):
         return self.nama
    
    class meta :
        verbose_name_plural = "Kategori"

class Artikel(models.Model):
    nama = models.CharField(max_length=100,blank=True,null=True)
    judul = models.CharField(max_length=100)
    body = models.TextField()
    kategori = models.ForeignKey(Kategori, on_delete=models.CASCADE, blank=True,null=True)
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return "{} - {}".format(self.nama, self.judul)
    
    class meta :
        ordering = ['-id']
        verbose_name_plural = "Artikel"
class Doa(models.Model):
    id = models.IntegerField(primary_key=True)
    doa = models.CharField(max_length=100)
    ayat = models.CharField(max_length=1000)
    latin = models.TextField()
    artinya = models.TextField()
    
    def __str__(self):
        return "{} - {}".format(self.doa, self.id)
    
class Sholat(models.Model):
    tanggal = models.DateField()
    imsyak = models.TimeField()
    shubuh = models.TimeField()
    terbit = models.TimeField()
    dhuha = models.TimeField()
    dhuhur = models.TimeField()
    ashr = models.TimeField()
    magrib = models.TimeField()
    isya = models.TimeField()
    
    def __str__(self):
        return "{} - {}".format(self.tanggal, self.terbit)
    
    