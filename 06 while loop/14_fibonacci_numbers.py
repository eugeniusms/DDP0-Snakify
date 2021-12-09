#Menginisiasi cek[0] = 0 dan cek[1] = 1, juga memberi input number
number = int(input())
cek = [0, 1]

#Mengoperasikan rumus fibonacci dengan array (dari bawah)
for i in range(number):
    cek[i] = cek[i] + cek [i + 1]
    cek.append(cek[i])

#Memanggil cek index number untuk diprint
print(cek[number])
