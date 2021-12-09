#Membuat variabel input
lst = input()

#Membuat pecahan bagian ke list dan membuat variabel inisiasi untuk n
bilangan = list(map(int, lst.split()))
n = 0

#Membuat proses print jika list n+1 > n dengan jarak antara print -> end = " "
while n <= len(bilangan)-2:
    if bilangan[n] < bilangan[n+1]:
        print(bilangan[n+1], end = " ")
    n += 1
