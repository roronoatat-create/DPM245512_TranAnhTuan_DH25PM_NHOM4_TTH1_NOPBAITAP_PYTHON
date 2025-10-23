#Câu 7: Tính và xuất độ dài đoạn AB
from math import sqrt

print("Chương trình tính độ dài đoạn AB")

print("--- Nhập tọa độ điểm A ---")
xA = float(input("Nhập xA: "))
yA = float(input("Nhập yA: "))

print("--- Nhập tọa độ điểm B ---")
xB = float(input("Nhập xB: "))
yB = float(input("Nhập yB: "))

do_dai = sqrt((xB - xA)**2 + (yB - yA)**2)

print(f"Độ dài đoạn AB = {do_dai}")