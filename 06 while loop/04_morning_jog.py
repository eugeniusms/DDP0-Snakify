#Membuat input jarak hari pertama lari dan jarak harus ditempuh
first = int(input())
target = int(input())

#Membuat set hari dimulai start hari pertama day 1
day = 1

#Membuat perhitungan matematis jarak dari hari ke hari
while first < target:
    next = first * 0.1 
    first += next
    day += 1
else:
    print(day)