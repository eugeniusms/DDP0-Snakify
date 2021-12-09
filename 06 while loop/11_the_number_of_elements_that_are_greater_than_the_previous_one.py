#Membuat inisiasi angka -> utama (besar agar tidak ada yg lebih), angka_2 sebagai angka pembanding, count untuk mengecek jumlah angka > angka sebelum
angka = 1000000
angka_2 = 0
count = 0

#Jika "0" sudah muncul maka program akan lari ke print saja
while angka != 0:
    #Mengisi angka_2 dengan angka sebelumnya
    angka_2 = angka
    angka = int(input())
    #Jika angka baru lebih besar dari angka sebelumnya maka tulis count bertambah 1
    if angka > angka_2:
        count += 1

print(count)
