#Membuat input batas bawah dan atas
start = int(input())
end = int(input())

#Membuat algoritma for in range
#Ketika start < end maka program berjalan maju
if start < end:
    for x in range(start, end+1):
        print(x)
#Ketika start > end maka program berjalan terbalik
elif start > end:
    for x in range(start, end-1, -1):
        print(x)
#Ketika start == end maka output adalah bilangan itu sendiri
elif start == end:
    print(start)
