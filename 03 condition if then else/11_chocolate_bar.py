#Memberi variabel koordinat awal (a,b) dan koordinat akhir (x,y)
a = int(input())
b = int(input())
x = int(input())
y = int(input())

#Mengecek perpindahan tiap komponen koordinatnya dengan nilai mutlak dari pengurangan -> selisih
komponen_x = abs(a - x)
komponen_y = abs(b - y)

#Jika perpindahan pada tiap komponennya lebih dari 2 maka tidak memenuhi syarat pindah
#Jika perpindahan pada tiap komponen kurang dari 1 -> tetap ditempat pasti tidak memenuhi syarat pindah juga
cek = str()

if (komponen_x > 2 or komponen_y > 2) or (komponen_x < 1 or komponen_y < 1):
    print("NO")
else:
    cek = "AMAN"

#Menggunakan cek, jika program not AMAN maka program berhenti karena tidak memenuhi syarat
#Jika selisih komponen x = 1 maka selisih komponen y harus 2, begitu juga sebaliknya

if cek == "AMAN":
    if komponen_x == 1:
        if komponen_y == 2:
            print("YES")
        else:
            print("NO")
    elif komponen_x == 2:
        if komponen_y == 1:
            print("YES")
        else:
            print("NO")