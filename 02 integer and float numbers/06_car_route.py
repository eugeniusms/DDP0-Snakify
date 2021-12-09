#Terdapat dua variabel N dan M di mana N adalah jarak yang bisa ditempuh sehari dan M adalah input untuk jarak M diperlukan berapa hari

N = int(input())
M = int(input())

#Perhatikan terdapat dua kasus, kasus pertama adalah saat tepat habis dan kasus kedua adalah saat tidak tepat habis, untuk yang tidak tepat habis maka memerlukan pembulatan ke atas karena sudah berbeda hari

if M%N == 0:
    print(M//N)
else:
    print(M//N+1)