#Membuat input, memetakan input ke bentuk list, menginisiasi count untuk menghitung
word = input()
lst = list(map(int, word.split()))
count = 0

#Melakukan perulangan selama masih di bawah range
for i in range(len(lst) - 1):
    #Memenuhi syarat untuk i awal dan i akhir ga usah disertakan karena 1 tetangga aja
    if i == 0:
        i += 1
    #Mengakhiri program saat range selesai
    elif i == len(lst) - 1:
        break
    #Bentuk normal program berjalan di sini dengan pengecekan lebih besar dari nilai kanan kiri tidak
    else:
        if lst[i] > lst[i - 1] and lst[i] > lst[i + 1]:
            count += 1
    #Agar program berulang naik i += 1 ke atas for
    i += 1

print(count)
