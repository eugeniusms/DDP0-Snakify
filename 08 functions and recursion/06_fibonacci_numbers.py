#Membuat angka input
angka = int(input())

#Fungsi fibonacci
def fibonacci(angka):
    if angka != 1:
        basis_0 = 0
        basis_1 = 1
        basis_2 = 0
        for i in range(angka - 1):
            #Melakukan pertambahan dengan pertukaran basis_0 untuk n - 2, basis_1 untuk n - 1, dan basis_2 untuk n dalam Un
            basis_2 = basis_1 + basis_0
            basis_0 = basis_1
            basis_1 = basis_2
        return basis_2
    else:
        return 1

#Memanggil fungsi fibonacci
print(fibonacci(angka))