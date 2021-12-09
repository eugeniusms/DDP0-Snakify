#Membuat variabel menit terlebih dahulu

menit = int(input())

#Membuat konversi menjadi jam dan menit

jam = menit//60
menit%=60

print(str(jam)+" "+str(menit))