#operator aritmatika

print("Total stok buah hari ini:")
apel = 7
jeruk = 9
totalBuah = apel + jeruk
print("Jumlah apel dan jeruk adalah:", totalBuah)

utangSupplier = 10000
bayarHariIni = 5000
sisaUtang = utangSupplier - bayarHariIni
print("Sisa utang ke supplier adalah:", sisaUtang)

panjangMeja = 15
lebarMeja = 8
luasMeja = panjangMeja * lebarMeja
print("Luas meja pajang buah:", luasMeja, "cm persegi")

jumlahKue = 16
jumlahPelanggan = 4
kuePerPelanggan = jumlahKue / jumlahPelanggan
print("Setiap pelanggan mendapat", kuePerPelanggan, "kue")

totalKue = 14
orang = 5
sisaKue = totalKue % orang
print("Sisa kue yang tidak terbagi adalah:", sisaKue)

tingkatRak = 2
jumlahRakPerTingkat = 8
kapasitasTotal = jumlahRakPerTingkat ** tingkatRak
print("Total kapasitas rak buah:", kapasitasTotal)

totalBuahMasuk = 10
buahPerDus = 3
jumlahDus = totalBuahMasuk // buahPerDus
print("Jumlah dus penuh yang bisa dibuat:", jumlahDus)


#Operator Perbandingan

#Sama dengan (==)
print('Operator sama dengan')
print('2 == 2 bernilai', 2==2)
print('3 == 2 bernilai', 3==2)
print()

#Tidak sama dengan (!=)
print('Operator tidak sama dengan')
print('2 != 2 bernilai', 2!=2)
print('3 != 2 bernilai', 3!=2)
print()

#Lebih besar dari (>)
print('Operator lebih besar dari')
print('5 > 3 bernilai', 5>3)
print('5 > 10 bernilai', 5>10)
print()

#Lebih kecil dari (<)
print('Operator lebih kecil dari')
print('5 < 3 bernilai', 5<3)
print('5 < 10 bernilai', 5<10)
print()

#Lebih besar dari (>=)
print('Operator lebih besar dari')
print('5 >= 10 bernilai', 5>=10)
print('5 >= 5 bernilai', 5>=5)
print('5 >= 3 bernilai', 5>=3)
print()

#Lebih kecil dari (<=)
print('Operator lebih kecil dari')
print('5 <= 3 bernilai', 5<=3)
print('5 <= 5 bernilai', 5<=5)
print('5 <= 10 bernilai', 5<=10)
print()


#Operator Penugasan

#Sama dengan (=)
print('Operator sama dengan')
a = 2
print(a)
b = 2.5
print(b)
a = b
print(a)

#Tambah sama dengan (+=)
print('Operator tambah sama dengan')
a = 2
print(a)
a += 5
a = a + 5
print(a)
print()

#Kurang sama dengan (-=)
print('Operator kurang sama dengan')
a = 4
print(a)
a -= 2
print(a)
print()

#Kali sama dengan (*=)
print('Operator kali sama dengan')
a = 4
print(a)
a *= 2
print(a)
print()

#Bagi sama dengan (/=)
print('Operator bagi sama dengan')
a = 4
print(a)
a /= 2
print(a)
print()

#Sisa bagi sama dengan (%=)
print('Operator sisa bagi sama dengan')
a = 7
print(a)
a %= 2
print(a)
print()

#Pangkat sama dengan (**=)
print('Operator pangkat sama dengan')
a = 4
print(a)
a **= 2
print(a)
print()

#Pembagian bulat sama dengan (//=)
print('Operator sisa bagi sama dengan')
a = 10
print(a)
a //= 3
print(a)
print()


#Operator Logical

#and
print('5>3 dan 5>2 bernilai', 5>3 and 5>2)
print('5>3 dan 5>10 bernilai', 5>3 and 5>10)
print('5>10 dan 5>3 bernilai', 5>10 and 5>3)
print('5>10 dan 5>8 bernilai', 5>10 and 5>8)
print()

#or
print('5>3 atau 5>2 bernilai', 5>3 or 5>2)
print('5>3 atau 5>10 bernilai', 5>3 or 5>10)
print('5>10 atau 5>3 bernilai', 5>10 or 5>3)
print('5>10 atau 5>8 bernilai', 5>10 or 5>8)
print()

#not
print(not 5>3)
print(not 1>3)


#Operator Bitwise

a = 13 #dalam biner bernilai 0000 1101
b = 37 #dalam biner bernilai 0010 0101
c = a & b #akan bernilai     0000 0101
print(c)
print()

a = 13 #dalam biner bernilai 0000 1101
b = 37 #dalam biner bernilai 0010 0101
c = a | b #akan bernilai     0010 1101
print(c)


#Operator Keanggotaan

sebuah_list = [1,2,3,4,5]
print('sebua_list =', sebuah_list)
print('5 in sebuah_list bernilai', 5 in sebuah_list)
print('10 in sebuah_list bernilai', 10 in sebuah_list)
print()

#not in
sebuah_list = [1,2,3,4,5]
print('sebua_list =', sebuah_list)
print('5 not in sebuah_list bernilai', 5 not in sebuah_list)
print('10 not in sebuah_list bernilai', 10 not in sebuah_list)

#Operator Identitas
#is
a, b, c = 10, 10, 5
print('a =', a)
print('b =', b)
print('c =', c)
print('a is b bernilai', a is b)
print('a is c bernilai', a is c)
print()

#is not
a, b, c = 10, 10, 5
print('a =', a)
print('b =', b)
print('c =', c)
print('a is not b bernilai', a is not b)
print('a is not c bernilai', a is not c)