#Membuat variabel kalimatnya
line = str(input())

#Melakukan konversi string ke list dengan pembatas split()
word = list(map(str, line.split()))

#Melakukan penukaran posisi word 1 dengan word 2 menggunakan variabel boneka imp
imp = word[1]
word[1] = word[0]
word[0] = imp

#Melakukan konversi list ke string lagi
print(" ".join(word))