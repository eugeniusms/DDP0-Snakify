#Membuat input angka kotak
angka = input()
kotak = list(map(int, angka.split()))
matriks = []
#Menginisiasi count
count = 0

#Selama perhitungan masih kurang dari jumlah baris baca inputnya terus
while count < kotak[0]:
    #Jika baris genap (mulai 0) maka kolom genap (mulai 0) harus "." dan kolom ganjil harus "*"
    if count % 2 == 0:
        for i in range(kotak[1]):
            if i % 2 == 0:
                print(".", end = " ")
            else:
                print("*", end = " ")
    else:
        #Jika baris ganjil (mulai 1) maka kolom genap (mulai 0) harus "*" dan kolom ganjil harus "."
        for i in range(kotak[1]):
            if i % 2 == 0:
                print("*", end = " ")
            else:
                print(".", end = " ")
    print("\n")
    count += 1




