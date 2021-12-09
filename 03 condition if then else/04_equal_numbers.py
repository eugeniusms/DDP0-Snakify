#Membaca input dari ketiga variabel
num_1 = int(input())
num_2 = int(input())
num_3 = int(input())

#Membuat perbandingan penunjuk kesamaan
if num_1 == num_2 and num_1 == num_3:
    print("3")
elif num_1 != num_2 and num_1 != num_3 and num_2 != num_3:
    print("0")
else:
    print("2")
