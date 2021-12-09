#Membuat variabel dari jam, menit, dan detik
jam = int(input())
menit = int(input())
detik = int(input())

#Setiap jamnya sudut jarum pendek bertambah 360/12 = 30, untuk setiap menitnya 360/(12*60) = 0.5, untuk setiap detiknya 360/(12*60*60) = 0.8333 
jam *= 30
menit *= 0.5
detik *= 0.00833333

#Karena jarum pendek berjalan maju pada setiap jam, menit, dan detiknya, maka jika terhitung sejak titik awal (pukul 12) tinggal menjumlahkan perkalian jam, menit, dan detik dengan sudut yang dihasilkan dari situ
print(jam+menit+detik)
