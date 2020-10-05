print("Nhap he so a va b: ")
a = float(input())
b = float(input())

if a==0:
    if b==0:
        print("Phuong trinh co vo so nghiem.")
    else:
        print("Phuong trinh vo nghiem.")
else:
    print("Phuong trinh co nghiem x = "+ '%.2f'%(-b/a))