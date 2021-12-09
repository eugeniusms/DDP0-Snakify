#Membuat inisiasi angka -> utama, angka_2 sebagai angka pembanding, max sebagai penyimpan sementara
angka = 1
angka_2 = 0
max = 0

#Jika "0" sudah muncul maka program akan lari ke print saja
while angka != 0:
    #Mengisi angka_2 dengan angka sebelumnya
    angka_2 = angka
    angka = int(input())
    #Jika angka baru lebih besar dari angka sebelumnya maka ubah max
    if angka > max:
        max = angka
        #Set same ke 1 jika ada yang lebih tinggi
        same = 1
    elif angka == max:
        same += 1

print(same)
