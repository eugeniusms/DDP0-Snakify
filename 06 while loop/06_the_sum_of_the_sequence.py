#Membuat inisiasi count untuk menghitung saat nol belum muncul dan angka 1 agar tidak nol (nilai boneka)
count = 0
angka = 1

#Jika "0" sudah muncul maka program akan lari ke print saja
while angka != 0:
  count += angka
  angka = int(input())

#Mengurangi dengan 1 karena 1 adalah basis nilai boneka
print(count - 1)
