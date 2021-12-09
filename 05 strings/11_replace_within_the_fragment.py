#Membuat input variabel untuk kata yang ingin difilter
word = str(input())
index = 0
index_reverse = 0

#Mencari index dari huruf h  dengan kata urut seperti urutan awal
index = word.find('h')

if word.count('h') > 1:
    #Mencari index dari huruf h dengan kata terbalik (untuk mencari yang belakang)
    index_reverse = len(word) - word[::-1].find('h') - 1

#Mengkapitalisasi h di antara h depan dan h belakang
new_word = word[index + 1:index_reverse].replace('h', "H")

#Membentuk ulang kata dengan awal sampai bertemu h pertama lalu menyelipkan antara yang sudah dengan kapital h kemudian ditutup dari h akhir sampai akhir
print(word[:index + 1] + new_word + word[index_reverse:])