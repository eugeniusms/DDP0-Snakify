#Untuk kasus 3 digit angka bisa kita bagi 3 kasus integer

nomor = str(input())

char_1 = nomor[:1:]
char_2 = nomor[1:2]
char_3 = nomor[2:3]

print(int(char_1)+int(char_2)+int(char_3))