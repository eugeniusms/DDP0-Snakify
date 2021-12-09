#Membuat variabel input pertama
lst = input()

#Memasukan nilai lst ke list bilangan dan membuat variabel kosong di bilangan_2
bilangan = list(map(int, lst.split()))
bilangan_2 = []

#Mengecek apakah x dalam bilangan terdapat di bilangan_2? Jika tidak maka tambahkan ke bilangan_2, dengan begini jika ada yang sama tidak akan ikut
for x in bilangan:
    if x not in bilangan_2:
        bilangan_2.append(x)

print(len(bilangan_2))