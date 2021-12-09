#Beri variabel nomor untuk input

nomor = str(input())

#Cari tahu jumlah karakter nomor

length = len(nomor)

#Lakukan slicing, jika diminta puluhannya maka itu berarti 2 dari belakang, jika 2 karakter startnya 0, jika 3 karakter startnya 1, maka start=karakter-2
   
start = length-2

#Jangan lupa memiliki end juga, jika 2 karakter endnya 1, jika 3 karakter endnya 2, maka end=karakter-1

end = length-1

#Buat syarat untuk satuan saja tidak akan menghasilkan jawaban
if length==1:
    print("0")
else:
    print(nomor[start:end:])