#Membuat input kata
word = str(input())

#Menindih setiap "@" dengan karakter kosong
word = word.replace("@", "")

print(word)