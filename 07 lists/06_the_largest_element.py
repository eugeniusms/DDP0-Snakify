#Membuat input, memetakan input ke bentuk list, max default minus biar menampung minus
word = input()
lst = list(map(int, word.split()))
max = -999999999999999

#Melakukan perulangan untuk mencari nilai max
for i in range(len(lst)):
    if lst[i] > max:
        max = lst[i]
    i += 1

#Mencari letak index pertama dari nilai max
index = lst.index(max)

print(max, index)