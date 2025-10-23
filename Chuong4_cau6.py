#Câu 6: Những giá trị nào có thể xuất hiện trong randrange(0, 100)
import random

print("--- Minh họa hàm randrange(0, 100) ---")
print("Hàm này trả về các số nguyên từ 0 đến 99.")
print("-" * 30)

print("5 Giá trị ngẫu nhiên được tạo ra:")
for i in range(5):
    random_value = random.randrange(0, 100)
    print(f"Lần {i+1}: {random_value}")

print("-" * 30)
print("Phạm vi giá trị:")
print(f"Giá trị nhỏ nhất có thể là 0. Ví dụ: {random.randrange(0, 1)}") 
print(f"Giá trị lớn nhất có thể là 99. Ví dụ: {random.randrange(99, 100)}")