#Membuat variabel sesuai soal
A = int(input())
B = int(input())
N = int(input())

#Memastikan bahwa A dan B diperbarui sesuai jumlahnya
A *= N
B *= N

#Mengetahui hasil dan sisa bagi B agar bisa diposisikan ke A atau B
A += B // 100 
B = B % 100

print(A, " ",B)
