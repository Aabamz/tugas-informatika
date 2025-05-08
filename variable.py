# proses memasukkan data ke dalam variabel
merk = "Toyota Supra"
# proses mencetak variabel
print(merk)

# nilai dan tipe data dalam variabel dapat diubah
tahun_produksi = 2020           # nilai awal
print(tahun_produksi)           # mencetak nilai tahun produksi
print(type(tahun_produksi))     # mengecek tipe data tahun_produksi
tahun_produksi = "dua ribu dua puluh"  # nilai setelah diubah
print(tahun_produksi)           # mencetak nilai tahun produksi
print(type(tahun_produksi))     # mengecek tipe data tahun_produksi

merk_awal = "Honda"
tipe = "Civic"
kendaraan = merk_awal + " " + tipe
tahun = 2022
jenis_bahan_bakar = "Bensin"
print("Data Kendaraan:\n", kendaraan, "\n", tahun, "\n", jenis_bahan_bakar)

# contoh variabel lainnya
warna_kendaraan = "Merah"
_transmisi = "Manual"
tipe_mesin123 = "VTEC Turbo"
kecepatan_maksimal = "220 km/jam"

panjang_kendaraan = 4.5  # dalam meter
lebar_kendaraan = 1.8    # dalam meter
luas_kendaraan = panjang_kendaraan * lebar_kendaraan
print(luas_kendaraan)