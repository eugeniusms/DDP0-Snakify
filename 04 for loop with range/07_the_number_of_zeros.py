#Membuat inisiasi count dan juga variabel input
number = int(input())
count = 0

#Melakukan perulangan angka sampai number
for i in range(number):
    angka = int(input())
    #Jika ada angka nol dalam input akan langsung ditambahkan dalam variabel count
    if angka == 0:
        count += 1

print(count)
