#input jam dalam variabel
jam = float(input())

#setiap jarak 1 jam memiliki sudut 30 derajat, sehingga sisanya bisa dianggap sisa dari 30 derajat itu yang dikalikan 12 karena pada jam terdapat 12 angka untuk mengelilingi
print(jam % 30 * 12)