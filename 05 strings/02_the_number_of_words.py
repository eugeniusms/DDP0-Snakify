#Membuat variabel line untuk sebuah kalimat
line = str(input())

#Mencari kata tinggal menghitung tanda pemisah sebuah kata yaitu spasi
spasi = line.count(" ")

#Karena spasi terakhir tidak ada jadi kita tambah 1
print(spasi+1)
