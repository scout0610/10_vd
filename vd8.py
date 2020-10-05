import math

print("Nhap he so a,b va c: ")
a = float(input())
b = float(input())
c = float(input())

if a==0:
    if b==0:
        if c==0:
            print("Phuong trinh co vo so nghiem.")
        else:
            print("Phuong trinh vo nghiem.")

    else:
        print("phuong trinh co nghiem: " + '%.2f'%(-c/b))
else:
    d = b*b - 4*a*c
    if d<0:
        print("phuong trinh vo nghiem")
    elif d==0:
        print("phuong trinh co nghiem kep: "+'%.2f'%(-b/(2*a)))
    else:
        x1 = (-b - math.sqrt(d)) / (2 * a)
        x2 = (-b + math.sqrt(d)) / (2 * a)
        print("phuong trinh có 2 nghiem la: "+ '%.2f'%(x1)+" "+ '%.2f'%(x2))

