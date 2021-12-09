#Masukkan angka untuk input
angka = input()

#Ubah sets menjadi set untuk menghitung isi unik
sets = set(map(int, angka.split()))

#Menghitung jumlah isi tersisa sets
print(len(sets))
