#Membaca input bilangan bulat
num = int(input())

#Membuat default nilai untuk positif (1), negatif (-1), dan nol (0)
if num > 0:
    print("1")
elif num < 0:
    print("-1")
else:
    print("0")