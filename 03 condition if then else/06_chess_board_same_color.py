#Memberi variabel koordinat awal (a,b) dan koordinat akhir (x,y)
a = int(input())
b = int(input())
x = int(input())
y = int(input())

#Perhatikan jika warna akan gelap saat hasil penjumlahan komponen koordinatnya -> genap begitu pun sebaliknya
koordinat_awal = a + b
koordinat_akhir = x + y

#Mengecek apakah koordinat_awal dan koordinat_akhir sesama genap/ganjil atau beda dengan pembagian sisa (modulo)
if koordinat_awal % 2 == 0:
    if koordinat_akhir % 2 == 0:
        print("YES")
    else:
        print("NO")

if koordinat_awal % 2 != 0:
    if koordinat_akhir % 2 != 0:
        print("YES")
    else:
        print("NO")
       

