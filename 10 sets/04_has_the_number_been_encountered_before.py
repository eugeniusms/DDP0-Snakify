#Membuat input angka
angka = input()
#Mengubah angka menjadi sets untuk mencari angka unik, serta juga bentuk list agar masih bisa dilacak
sets = set(map(int, angka.split()))
angka = list(map(int, angka.split()))

#Mengubah ke bentuk list agar bisa dihitung indexnya
sets = list(sets)

#Melakukan perulangan, setiap ada yang sama (irisan), nilai selalu dihapus, sehingga jika tak ada (pernah ada) maka bisa dituliskan YES (nilainya sudah terhapus hilang sebelumnya)
for i in range(len(angka)):
    if angka[i] in  sets:
        sets.remove(angka[i])
        sets.append(" ")
        print("NO")
    else:
        print("YES")
    i += 1