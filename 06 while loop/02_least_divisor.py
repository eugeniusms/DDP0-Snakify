#Membuat input bilangan yang dicari pembagi terkecilnya
num = int(input())

#Membuat variabel boneka 
imp = 2

#Membuat program modulus 0
while num >= imp:
    if num % imp == 0:
        print(imp)
        break
    else:
        imp += 1