#Membuat input variabel jam_1, menit_1, detik_1

jam_1 = int(input())
menit_1 = int(input())
detik_1 = int(input())

#Membuat input variabel jam_2, menit_2, detik_2

jam_2 = int(input())
menit_2 = int(input())
detik_2 = int(input())

#ingat syarat input adalah waktu pertama sebelum waktu kedua sehingga memudahkan dalam memprogram, tinggal mengurangi saja dan mengonversi hasilnya

jam = jam_2-jam_1
menit = menit_2-menit_1
detik = detik_2-detik_1

jam*=3600
menit*=60

print(jam+menit+detik)
