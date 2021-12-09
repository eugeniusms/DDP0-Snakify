#Memberi variabel koordinat awal (a,b) dan koordinat akhir (x,y)
a = int(input())
b = int(input())
x = int(input())
y = int(input())

#Mengecek perpindahan tiap komponen koordinatnya dengan nilai mutlak dari pengurangan -> selisih
komponen_x = abs(a - x)
komponen_y = abs(b - y)

#Jika perpindahan pada tiap komponennya tidak lebih dari 1 maka operasi pemindahan dapat dilakukan
if komponen_x <= 1 and komponen_y <= 1:
    print("YES")
else:
    print("NO")