print("Nhap he so a,b va c: ")
a = float(input())
b = float(input())
c = float(input())

if a + b > c and a + c > b and b + c > a:
    print("Day la 3 canh cua tam giac.")
    if a == b and b == c:
        print("Day la tam giac deu.")
    elif a == b or b == c or a == c:
        print("Day la tam giac can.")
    elif a*a + b*b == c*c or a*a + c*c == b*b or b*b + c*c == a*a:
        print("Day la tam giac vuong.")
    else:
        print("Day la tam giac thuong")
else:
    print("Day khong phai la 3 canh cua tam giac.")
