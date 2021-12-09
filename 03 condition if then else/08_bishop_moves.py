#Memberi variabel koordinat awal (a,b) dan koordinat akhir (x,y)
a = int(input())
b = int(input())
x = int(input())
y = int(input())

#Mengecek perpindahan tiap komponen koordinatnya dengan nilai mutlak dari pengurangan -> selisih
komponen_x = abs(a - x)
komponen_y = abs(b - y)

#Jika perpindahan pada tiap komponennya berselisih sama artinya mereka berpindah secara diagonal vektor(n,n) dan ini dapat dilakukan perpindahan
if komponen_x == komponen_y:
    print("YES")
else:
    print("NO")