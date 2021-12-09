#Membuat bilangan inisiasi untuk difaktorialkan
angka = int(input())

#Membuat inisiasi untuk nilai hasil
hasil = 1

#Membuat perkalian dari bawah (tidak seperti faktorial biasanya, versi reverse jauh lebih mudah)
for i in range(angka):
    hasil *= (i+1)

print(hasil)