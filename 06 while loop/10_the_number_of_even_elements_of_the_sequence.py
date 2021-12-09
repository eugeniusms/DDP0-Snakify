#Membuat inisiasi angka -> utama, count untuk menghitung angka genap
angka = 1
count = 0

#Jika "0" sudah muncul maka program akan lari ke print saja
while angka != 0:
    angka = int(input())
    if angka % 2 == 0:
        count += 1

#Mengurangi - 1 karena 0 terhitung genap
print(count - 1)