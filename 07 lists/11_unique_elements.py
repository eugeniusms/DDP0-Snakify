#Membuat input, memetakan input ke bentuk list, menginisiasi count dan same untuk menyimpan jumlah dari beberapa nilai sementara, hitung menghitung total hasil
word = input()
lst = list(map(int, word.split()))
count = 0
same = []


#Melakukan perulangan berlapis -> pencocokan data satu per satu, jika sama tambahkan dalam count
for i in range(len(lst)):
    for j in range(len(lst)):
        if lst[i] == lst[j]:
            count += 1
        j += 1
    #Mendapatkan jumlah dari beberapa nilai yang sama
    same.append(count)
    i += 1
    count = 0

#Print untuk nilai same = 1
for x in range(len(same)):
    if same[x] == 1:
        print(lst[x], end = " ")