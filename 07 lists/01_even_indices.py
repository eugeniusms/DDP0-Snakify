#Membuat variabel input
lst = input()

#Gunakan fungsi map untuk konversi menjadi list atau iterable baru 
#Fungsi split untuk memisahkan string dan menambahkan data ke array string menggunakan pemisah yang didefinisikan
bilangan = list(map(int, lst.split()))

#Membuat variabel list kosong untuk diisi hasil
hasil = []
n = 0

#Membuat perulangan pencetakan hasil
while n <= len(bilangan)-1:
  hasil.append(bilangan[n])
  #Membuat agar selisih 2 (ganjil saja jadinya) saat program dijalankan
  n = n + 2
  #Merapikan program menjadi bentuk yang dimau
print(str(hasil).replace(',','').replace('[','').replace(']',''))