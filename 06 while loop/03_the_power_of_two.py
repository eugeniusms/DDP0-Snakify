#Membuat input bilangan dan menginisiasi basis dan count
number = int(input())
basis = 1
count = 0

#Lakukan pemangkatan dengan dua ketika basis <= number
while basis <= number:
    basis *= 2
    count += 1

#Membagi basis dan mengurangi count karena mereka hasil operasi terakhir saat batas max sebelum basis <= number
basis /= 2
count -= 1

print(count, " ", int(basis))