#Memberi variabel koordinat awal (a,b) dan koordinat akhir (x,y)
a = int(input())
b = int(input())
x = int(input())
y = int(input())


#Perhatikan langkah queen seperti gabungan bishop dan rook sehingga kita bisa langsung saja gunakan gabungannya untuk memastikan pergerakannya

#(ROOK MOVE) Membuat program cek jika sama baik salah satu koordinat antara a = x atau b = y, maka benteng bisa berpindah dalam satu langkah
if a == x or b == y:
    cek_rook = "YES"
else:
    cek_rook = "NO"

#Mengecek perpindahan tiap komponen koordinatnya dengan nilai mutlak dari pengurangan -> selisih
komponen_x = abs(a - x)
komponen_y = abs(b - y)

#(BISHOP MOVE) Jika perpindahan pada tiap komponennya berselisih sama artinya mereka berpindah secara diagonal vektor(n,n) dan ini dapat dilakukan perpindahan
if komponen_x == komponen_y:
    cek_bishop = "YES"
else:
    cek_bishop = "NO"

if cek_rook == "YES" or cek_bishop =="YES":
    print("YES")
else:
    print("NO")