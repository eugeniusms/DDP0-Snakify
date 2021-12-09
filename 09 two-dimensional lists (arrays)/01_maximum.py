#Membuat input angka kotak
angka = input()
kotak = list(map(int, angka.split()))
matriks = []
#Menginisiasi count
count = 0

#Selama perhitungan masih kurang dari jumlah baris baca inputnya terus
while count < kotak[0]:
    baris = input()
    baris_list = list(map(int, baris.split()))
    matriks.append(baris_list)
    count += 1

#Inisiasi basis
basis = -9999999999999999999

#Menenetukan nilai tertinggi dalam nested list
for i in range(len(matriks)):
    for j in range(len(matriks[i])):
        if matriks[i][j] > basis:
            basis = matriks[i][j]

#Menginisiasi index max dengan save
save = []

#Mencari index tiap nilai max
for i in range(len(matriks)):
    if basis in matriks[i]:
        for j in range(len(matriks[i])):
            if basis == matriks[i][j]:
                save.append(i)
                save.append(j)

#Hanya print yang paling dekat dengan pojok kiri
print(save[0], save[1])



    