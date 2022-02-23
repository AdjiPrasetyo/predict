from django.contrib import admin

# Register your models here.
from import_export.admin import ImportExportModelAdmin
from .models import Dataset

@admin.register(Dataset)
class DatasetsAdmin(ImportExportModelAdmin):
    list_display = ("tahun","bulan","curah_hujan","umur","luas_lahan", "jumlah_pokok", "jumlah_tandan", "rata_berat", "hasil_produksi")
    pass
