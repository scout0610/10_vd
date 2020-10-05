import numpy

print("Nhap 3 diem Toan, Ly, Hoa: ")

score = []
for i in range(0,3):
    x = float(input())
    score.append(x)
print("diem trung binh la: " + str(numpy.mean(score)))
print("diem cao nhat la: " + str(max(score)))
print("diem cao nhat la: " + str(min(score)))


