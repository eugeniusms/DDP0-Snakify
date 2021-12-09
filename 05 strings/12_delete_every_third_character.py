#Membuat variabel input dan mencari string step 3 dari input
word = str(input())
panjang = len(word)

#Untuk tiap substring dengan index hasil bagi == 0 maka akan hilang direplace dengan ""
for i in range(panjang):
    if i % 3 == 0:
        word = word.replace(word[i], "", 1)
        #Menambahkan spasi agar len panjang tetap berjalan normal (len string tidak berkurang)
        word = " " + word

#Menghapus spasi yang ada sebagai boneka
print(word.replace(" ", ""))