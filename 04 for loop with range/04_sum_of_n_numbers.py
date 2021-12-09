#Membuat input angka yang mau dihitung
total = int(input())

#Menginiasi list num kosong
num = []

#Membuat input sebanyak berapa kali
for x in range(total):
    imp = int(input())
    num.append(imp)

#Menulis hasil penjumlahan isi list
print(sum(num))
