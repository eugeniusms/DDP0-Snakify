#Membuat variabel angka, menginisiasi 2 list
number = int(input())
lst = []
biglst = []

#Memasukkan perulangan angka ke dalam lst
for i in range(number):
    lst.append(i+1)

#Memasukkan perulangan lst ke dalam big.lst dalam bentuk sesuai start,end, dan stepnya
for x in range(len(lst)):
   biglst.append((lst[:x+1:]))

#Melakukan pengubahan type list menjadi stringa agar bisa replace pada beberapa substring list
print(str(biglst).replace('[',"").replace(' ',"").replace(',',"").replace(']',"\n"))

