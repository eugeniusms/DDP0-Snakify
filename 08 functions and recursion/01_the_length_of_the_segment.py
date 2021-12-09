import math

#memasukan input koordinat
x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

#Membuat fungsi
def distance(x1, y1, x2, y2):
    #Menggunakan pythagoras jarak antar komponen untuk mencari jarak titik
    distance = math.sqrt(( x2 - x1 ) ** 2 + (y2 - y1)  ** 2)
    return distance

#Memanggil fungsi
print(distance(x1, y1, x2, y2))