
print("Nhap nam bat ky (so nguyen > 0): ")
year = int(input())

if year % 4 != 0:
    print("Day khong phai la nam nhuan.")
elif year % 100 != 0:
    print("Day la nam nhuan")
elif year % 400 != 0:
    print("Day khong phai la nam nhuan.")
else:
    print("Day la nam nhuan")

