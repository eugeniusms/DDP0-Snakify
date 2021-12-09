#Membuat variabel input tahun
year = int(input())

#Menyusun program dari pembagi luar(luas) ke -> dalam(khusus) yaitu pembagian 4 kemudian 100, baru pembagian dengan 400
if year % 4 == 0:
    if year % 100 == 0:
        #Jika hanya memenuhi pembagian 100 tapi tidak memenuhi pembagian 400 ataupun pembagian 4 maka terhitung COMMON
        if year % 400 == 0:
            print("LEAP")
        else:
            print("COMMON")
    #Jika tidak bisa dibagi 100 tapi bisa dibagi 4 tetap LEAP
    if year % 100 != 0:
        print("LEAP")
else:
    print("COMMON")
