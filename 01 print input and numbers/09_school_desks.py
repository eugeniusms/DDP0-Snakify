#Untuk genap pasti memiliki hasil mod = 0 jika dibagi 2, sedangkan untuk ganjil memiliki hasil mod = 1 jika dibagi 2 sehingga bisa ditentukan genap/ganjilnya. Variabel a, b, dan c sebagai kelas.

a = int(input())
b = int(input())
c = int(input())

#Untuk genap mudah saja tinggal floor division didapati bilangan bulat, sedangkan untuk ganjil perlu menambah 1 agar didapati meja pas (ada satu meja dengan satu anak)

if(a%2 == 0):
    a//=2
else:
    a//=2
    a+=1

if(b%2 == 0):
    b//=2
else:
    b//=2
    b+=1

if(c%2 == 0):
    c//=2
else:
    c//=2
    c+=1

print(a+b+c)
