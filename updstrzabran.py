peserta = 'Bagus Mas'
print('Nama sebelum diproses =', peserta)

# Menambahkan nama tengah "Satya"
peserta_lengkap = peserta[:5] + ' Satya ' + peserta[6:]
# [:5] = ambil dari awal sampai indeks ke-4 (yaitu 'Bagus')
# [6:] = ambil dari indeks ke-6 hingga akhir (yaitu 'Mas')
print('Nama setelah diproses =', peserta_lengkap)

# Menukar posisi nama belakang dan depan
nama_tertukar = peserta[6:] + " " + peserta[:5]
print('Nama setelah ditukar urutan =', nama_tertukar)
