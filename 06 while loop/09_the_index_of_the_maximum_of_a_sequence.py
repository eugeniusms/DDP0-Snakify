#Membuat inisiasi angka -> utama, angka_2 sebagai angka pembanding, max sebagai penyimpan sementara, count untuk mengecek program berjalan berapa jauh
angka = 1
angka_2 = 0
max = 0
count = 0

#Jika "0" sudah muncul maka program akan lari ke print saja
while angka != 0:
    #Mengisi angka_2 dengan angka sebelumnya
    angka_2 = angka
    angka = int(input())
    count += 1
    #Jika angka baru lebih besar dari angka sebelumnya maka ubah max, tulis count ke dalam index saat berada di situ
    if angka > max:
        max = angka
        index = count

print(index)
