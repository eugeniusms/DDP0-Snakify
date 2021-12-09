#Membaca bilangan float terlebih dahulu lalu diubah ke bentuk string untuk melakukan slicing

angka = float(input())
karakter = str(angka)

#Untuk mendapatkan angka pertama setelah desimal, maka kita cari panjang dari karakter depan titik dahulu agar bisa dicari startnya

bulat = int(angka)
length = len(str(bulat))

#Letak karakter pertama setelah titik berada di length+1 karena terdapat jeda satu titik, sehingga start=length+1

start = length+1

#Karena end saat setelahnya, maka end=start+1

end = start+1

print(karakter[start:end:])