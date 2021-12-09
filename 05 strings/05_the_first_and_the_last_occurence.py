#Membuat input variabel untuk kata yang ingin difilter
word = str(input())
index = 0
index_reverse = 0

if word.count('f') == 0:
    print(" ")
else:
    #Mencari index dari huruf f dengan kata urut seperti urutan awal
    index = word.find('f')
    print(index, end = " ")

if word.count('f') > 1:
    #Mencari index dari huruf f dengan kata terbalik (untuk mencari yang belakang)
    index_reverse = len(word) - word[::-1].find('f') - 1
    print(index_reverse)