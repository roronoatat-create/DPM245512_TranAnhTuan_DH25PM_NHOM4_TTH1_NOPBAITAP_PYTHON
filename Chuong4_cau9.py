#Câu 9: Viết chương trình tính căn bậc 2 lồng nhau
from math import sqrt

print("Chương trình tính S(n) = Căn(2 + Căn(2 + ...))")
n = int(input("Nhập n (số dấu căn lồng nhau): "))

S = 0.0

if n <= 0:
    print("n phải là số nguyên dương")
else:
    for _ in range(n):
        S = sqrt(2 + S)
    
    print(f"Kết quả S({n}) = {S}")