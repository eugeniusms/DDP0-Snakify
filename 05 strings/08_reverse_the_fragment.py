#Membuat input variabel untuk kata yang ingin difilter
word = str(input())
index = 0
index_reverse = 0

#Mencari index dari huruf h  dengan kata urut seperti urutan awal
index = word.find('h')

if word.count('h') > 1:
    #Mencari index dari huruf h dengan kata terbalik (untuk mencari yang belakang)
    index_reverse = len(word) - word[::-1].find('h') - 1

#Membagi kasus dengan h di awal dan di akhir juga untuk yang sebaliknya karena nilai end ekslusif -> h bisa ilang
#Print dari awal kata sampai h pertama ditambah print antara h dengan step -1 untuk membalik ditambah dari h kedua + 1 sampai akhir 
if word.find('h') == 0:
    print(word[:index + 1] + word[index_reverse - 1:index:-1] + word[index_reverse:])
else:
    print(word[:index] + word[index_reverse:index - 1:-1] + word[index_reverse + 1:])