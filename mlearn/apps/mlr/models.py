from django.db import models
from django_pandas.managers import DataFrameManager

class Dataset(models.Model):
    tahun = models.IntegerField()
    bulan = models.IntegerField()
    curah_hujan = models.IntegerField()
    umur = models.IntegerField()
    luas_lahan = models.FloatField()
    jumlah_pokok = models.IntegerField()
    jumlah_tandan = models.IntegerField()
    rata_berat = models.FloatField()
    hasil_produksi = models.FloatField()


    objects = DataFrameManager()

    def __int__(self):
        return self.umur