#Beri variabel angka pada input
angka = int(input())

#Beri variabel next untuk angka selanjutnya dan prev untuk sebelumnya
next = angka+1
prev = angka-1

#ingat hanya bisa digabungkan saat menjadi string (str)
print("The next number for the number "+str(angka)+" is "+str(next)+".")
print("The previous number for the number "+str(angka)+" is "+str(prev)+".")
