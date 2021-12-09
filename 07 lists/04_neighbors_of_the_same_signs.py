#Membuat input, memetakan input ke bentuk list
word = input()
lst = list(map(int, word.split()))

#Melakukan perulangan selama belum menemukan tanda sesuai (ditandai dengan lst > 0 atau lst < 0)
for i in range(len(lst) - 1):
    if i == len(lst) - 1:
        print(" ")
        break
    else:
        if lst[i] > 0:
            #Saat angka sebelum dan sesudah sama-sama di atas 0 maka print dan break
            if lst[i + 1] > 0:
                print(lst[i], lst[i + 1])
                break
            else:
                #Saat angka belum sama lakukan perulangan lagi
                i += 1
        else:
            #Saat angka sebelum dan sesudah sama-sama di bawah 0 maka print dan break
            if lst[i + 1] < 0:
                print(lst[i], lst[i + 1])
                break
            else:
                #Saat angka belum sama lakukan perulangan lagi
                i += 1