#Membuat input kalimat
word = str(input())
#Memasukkan per kata ke dalam list untuk dicapitalize satu per satu
lst = list(map(str, word.split()))

#Membuat fungsi capitalize untuk setiap pemanggilan kata dalam lst
def capitalize(word):
    word = str(word).capitalize()
    return word

#Membuat perulangan sampai seluruh kata dalam lst mendapat capitalize dalam fungsi
for x in range(len(lst)):
    print(capitalize(lst[x]),end = " ")