#Membuat input untuk jumlah kartu dimainkan
card = int(input())

#Menginisiasi nilai total utuh dan yang tersedia
total = 0
available = 0

#Menghitung total jumlah jika kartu utuh
for i in range(card):
    total += (i+1)

#Menghitung total jumlah kartu yang tersedia
for i in range(card-1):
    available += int(input())

#Mencari kartu yang hilang tinggal dilihat selisih kartu asli jika utuh - kartu tersedia
print(total-available)
