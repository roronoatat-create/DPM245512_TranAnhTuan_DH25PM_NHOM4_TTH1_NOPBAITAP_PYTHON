#Câu 8: Viết chương trình tính logax
from math import log

print("Chương trình tính logarit cơ số a của x")

x = float(input("Nhập số x (x > 0): "))
a = float(input("Nhập cơ số a (a > 0 và a != 1): "))

if x <= 0:
    print("Giá trị x phải lớn hơn 0")
elif a <= 0 or a == 1:
    print("Cơ số a phải lớn hơn 0 và khác 1")
else:
    ket_qua = log(x, a)
    print(f"Logarit cơ số {a} của {x} là: {ket_qua}")