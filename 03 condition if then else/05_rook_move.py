#Membuat input lokasi awal benteng (a,b)
a = int(input())
b = int(input())

#Membuat input lokasi setelah berpindah (x,y)
x = int(input())
y = int(input())

#Membuat program cek jika sama baik salah satu koordinat antara a = x atau b = y, maka benteng bisa berpindah dalam satu langkah
if a == x or b == y:
    print("YES")
else:
    print("NO")