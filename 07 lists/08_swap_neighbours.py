#Membuat input, memetakan input ke bentuk list
word = input()
lst = list(map(int, word.split()))
imp = 0

#Melakukan perulangan selama masih di bawah range
for i in range(len(lst) - 1):
    if i % 2 == 0:
        imp = lst[i]
        lst[i] = lst[i + 1]
        lst[i + 1] = imp

#Mengubah lst ke bentuk string dan dilakukan replace pada objek kurang perlu
print(str(lst).replace("[","").replace("]","").replace(",",""))