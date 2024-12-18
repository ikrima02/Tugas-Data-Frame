#  nomor 1 
import pandas as pd
file_path = 'disperkim-od_16985_jumlah_produksi_sampah_berdasarkan_kabupatenkota_v3_data.xlsx'
data_sampah_kota_bandung = pd.read_excel(file_path, sheet_name='data')

df_sampah_kota_bandung = data_sampah_kota_bandung[['nama_kabupaten_kota', 'jumlah_produksi_sampah', 'satuan', 'tahun']]
print("Data Produksi Sampah Jawa Barat:")
df_sampah_kota_bandung

