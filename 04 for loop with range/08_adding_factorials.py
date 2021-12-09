#Menginisiasi nilai total = 0, nilai i = 1, nilai hasil = 1 dan membuat variabel angka
number = int(input())
total = 0
i = 1
hasil = 1

#Melakukan perulangan pada tiap angkanya
for i in range(number+1):
    #Melakukan faktorial sampai angka 1
    while i > 0:
        hasil *= i
        i -= 1
    #Memasukan hasil ke total
    total += hasil
    #Membuat set hasil ke 1 agar jika dikalikan while nanti tidak tercampur i yang lain
    hasil = 1

#Melakukan pengurangan dengan 1 karena set hasil awalnya 1 (digunakan untuk mengalikan) tetapi tidak terhitung
print(total-1)