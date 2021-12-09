#Membuat input variabel
lst = input()

#Memotong bagian variabel menjadi list dengan split() dan map()
bilangan = list(map(int, lst.split()))
hasil = []
n = 0

#Melakukan pengecekan bilangan genap habis dibagi 2
for n in bilangan:
    if n % 2 == 0:
        hasil.append(n)

#Mengeluarkan output dan merubah bentuk list menjadi bentuk biasa
print(str(hasil).replace(',','').replace('[','').replace(']',''))
        