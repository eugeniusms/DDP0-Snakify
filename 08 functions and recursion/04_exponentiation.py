#Membuat input a dan n
a = float(input())
n = int(input())

#Membuat fungsi perpangkatan
def power(a, n):
    a **= n
    return a

#Memanggil fungsi 
print(power(a, n))