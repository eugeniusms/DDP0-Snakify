#Menginisiasi berbagai variabel
angka = 1
count = 0
max = 0
lst = []

#Memasukan input ke dala list selama angka != 0
while angka != "0":
    angka = input()
    lst.append(angka)
    
lst.remove("0")

if len(lst) > 2:
    #Mencari angka berurutan yang sama
    for i in range(len(lst) -1 ):
        if lst[i + 1] == lst[i]:
            count += 1
            #Jika ternyata angka baru lebih banyak yg sama, maka berhak menggantikan max
            if count > max:
                max = count
        else: 
            #Set ulang count kesamaan ke 1
            count = 1
    #Saat indeks depan sama dengan indeks berikutnya maka terhitung tambah 1 karena eksklusif
    if lst[0] == lst[1]:
        print(max + 1)
    #Default untuk max = 0 (tak ada yang sama)
    elif max == 0:
        print("1")
    else:
        print(max)
else:
    print("1")
    

