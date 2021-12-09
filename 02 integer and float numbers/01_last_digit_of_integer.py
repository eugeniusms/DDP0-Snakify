#Beri input dengan nama nomor

nomor = str(input())

#Cari jumlah karakter dalam nomor dengan fungsi len()

length = len(nomor)

#Lakukan slicing dengan nilai start saja cukup, perhatikan untuk mendapatkan karakter terakhir dari 2 karakter start yg diperlukan = 1, sedangkan untuk 3 karakter diperlukan start = 2, maka start = karakter-1

start = length-1
print(nomor[start::])

