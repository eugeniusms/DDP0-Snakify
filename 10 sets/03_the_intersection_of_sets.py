#Masukkan angka untuk input baris 1 dan angka_2 untuk input baris 2
angka = input()
angka_2 = input()

#Ubah sets menjadi set untuk menghitung isi unik
sets = set(map(int, angka.split()))
sets_2 = set(map(int, angka_2.split()))

#Mengiris isi yang sama antara sets dan sets_2
sets_3 = sets.intersection(sets_2)

sort = sorted(sets_3)

#Mengubah list ke bentuk normal dengan replace objek list
print(str(sort).replace("[","").replace("]","").replace(",",""))
