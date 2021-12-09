#Membaca variabel kata terlebih dahulu

kata = str(input())

length = len(kata)
half = length//2

if length%2 != 0:
    
    part_1 = kata[:half:]
    part_2 = kata[half+1::]
    part_3 = kata[half:half+1:]

   # print(part_1)
   # print(part_2)
   # print(part_3)
    print(part_2+part_1+part_3)

elif length%2 == 0:
    
    print(kata[half:half+1:]+kata[half+1::]+kata[0:1:]+kata[1:half:])