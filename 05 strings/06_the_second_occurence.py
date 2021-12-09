#Membuat variabel untuk input kata
word = str(input())
index = 0
index_2 = 0

#Mengecek jika f tidak ada tuliskan -2, jika f hanya 1 tuliskan -1, dan jika ada lebih dari 1, tuliskan index f berikutnya
if word.count('f') == 0:
    print("-2")
elif word.count('f') == 1:
    print("-1")
else:
    index = word.find('f')
    #Mencari index berikutnya dengan nilai start adalah index sebelumnya ditambah 1 karena start inklusif
    index_2 = word.find('f', index + 1)
    print(index_2)
