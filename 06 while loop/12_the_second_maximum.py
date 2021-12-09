#Membuat inisiasi angka -> utama, max sebagai penyimpan sementara untuk max dan juga begitu dengan max_2, 
angka = 1
max = 0
max_2 = 0

#Jika "0" sudah muncul maka program akan lari ke print saja
while angka != 0:
    angka = int(input())
    #Jika angka baru lebih besar dari angka max_2 maka ubah max_2
    if angka > max_2:
        #Saringan berikutnya jika angka lebih besar dari max maka ubah max
        if angka > max:
            max_2 = max
            max = angka
        else:
            max_2 = angka
            
print(max_2)
