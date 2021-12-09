#Menginisiasi nilai total = 0
number = int(input())
total = 0
i = 1

#Melakukan proses pangkat 3 pada tiap i sekaligus penambahan nilai total pada setiap perulangannya
for i in range(number+1):
    total += (i**3)

print(total)