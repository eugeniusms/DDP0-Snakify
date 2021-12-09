#Membuat inisiasi count untuk menghitung saat nol belum muncul dan angka 1 agar tidak nol (nilai boneka) dan jumlah sebagai nilai penjumlahan input
jumlah = 0
count = 0
angka = 1

#Jika "0" sudah muncul maka program akan lari ke print saja
while angka != 0:
  jumlah += angka
  count += 1
  angka = int(input())

#Mengurangi dengan 1 karena 1 adalah basis nilai boneka, membagi jumlah dengan banyak input (count - 1 karena saat awal (angka boneka) count sudah terhitung)
print((jumlah - 1)/(count - 1))
