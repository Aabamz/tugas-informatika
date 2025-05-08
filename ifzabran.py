#Kondisi if adalah kondisi yang akan dieksekusi oleh program jika bernilai benar atau TRUE
suhu_tubuh = 39

#jika kondisi benar/TRUE maka program akan mengeksekusi perintah dibawahnya
if(suhu_tubuh > 37):
  print("Suhu Tubuh Di Atas Normal") # Kondisi Benar, Dieksekusi

#jika kondisi salah/FALSE maka program tidak akan mengeksekusi perintah dibawahnya
if(suhu_tubuh > 45):
  print("Suhu Tubuh Sangat Tinggi") # Kondisi Salah, Maka tidak tereksekusi


#Kondisi if else adalah jika kondisi bernilai TRUE maka akan dieksekusi pada if, tetapi jika bernilai FALSE maka akan dieksekusi kode pada else
usia = 17
#Jika pernyataan pada if bernilai TRUE maka if akan dieksekusi, tetapi jika FALSE kode pada else yang akan dieksekusi.
if(usia > 18):
    print("Termasuk Dewasa")
else:
    print("Termasuk Remaja")


detak_jantung = 63
if (detak_jantung >= 100):
  print('Sangat Cepat')
elif (detak_jantung >= 90):
  print('Cepat')
elif (detak_jantung >= 80):
  print('Normal Tinggi')
elif (detak_jantung >= 70):
  print('Normal')
elif (detak_jantung >= 60):
  print('Normal Rendah')
else:
  print('Lambat')
