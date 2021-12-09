#Menginisiasi isi cek, cek[2] = 1 untuk boneka saja begitu juga dengan i = 2 agar bisa segera dibandingkan dengan angka
angka = int(input())
cek = [0, 1, 1]
i = 2

while cek[i] != angka:
    #Membuat ketika sudah melebihi maka tak ada yang sama program berhenti dan i = 0, i - 1 = -1
    if cek[i] > angka:
        i = 0
        break
    #Saat program belum melebihi angka lakukan untuk menemukan kesempatan itu fibonacci
    else:
        cek[i] = cek[i - 1] + cek[i - 2]
        cek.append(cek[i])
        i += 1

#Karena i sudah tambah 1 saat masuk while else padahal ga perlu
print(i - 1)