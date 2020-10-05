print("Nhap so nguyen duong a: ")
a = int(input())
print("Nhap so nguyen duong n: ")
n = int(input())

bit = "{0:b}".format(a)

print(bit[n-1])
