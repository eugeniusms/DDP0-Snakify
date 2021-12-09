#Membuat input variabel untuk kata yang ingin difilter
word = str(input())
index = 0
index_reverse = 0

#Mencari index dari huruf h  dengan kata urut seperti urutan awal
index = word.find('h')

if word.count('h') > 1:
    #Mencari index dari huruf h dengan kata terbalik (untuk mencari yang belakang)
    index_reverse = len(word) - word[::-1].find('h') - 1

#Print dari awal kata sampai h pertama ditambah dari h kedua + 1 sampai akhir -> menghilangkan kata antara h
print(word[:index] + word[index_reverse + 1:])