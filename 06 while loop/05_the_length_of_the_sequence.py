#Membuat inisiasi count untuk menghitung saat nol belum muncul
count = 0

#Jika "0" sudah muncul maka program akan lari ke print saja
while str(input()) != "0":
  count += 1 

print(count)
