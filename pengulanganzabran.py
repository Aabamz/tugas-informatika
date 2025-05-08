#Contoh penggunaan While Loop
#Catatan: Penentuan ruang lingkup di Python bisa menggunakan tab alih-alih menggunakan tanda kurung

putaran = 0
while (putaran <= 9):
    print("Latihan ke:", putaran)
    putaran += 1

print ("Latihan selesai!")

#Contoh pengulangan for sederhana
nomor_peserta = [1,2,3,4,5]
for x in nomor_peserta:
    print("Peserta nomor", x)

#Contoh pengulangan for
makanan_sehat = ["pisang", "alpukat", "semangka"]
for y in makanan_sehat:
    print("Atlet disarankan makan", y)

# Menghitung hari latihan
for hari in range(1,12):
  print("Hari ke-", hari)

# outer loop
# Menampilkan tabel latihan beban (misal simulasi pengulangan set dan repetisi)
for set_ke in range(1, 11):
    # nested loop
    # untuk tiap repetisi dalam 1 set
    for repetisi in range(1, 11):
        # simulasi jumlah angkatan
        print(set_ke * repetisi, end=' ')
    print()
