#Câu 13: Hàm kiểm tra số hoàn thiện, số thịnh vượng
def tinh_tong_uoc_so(n):
    if n <= 1:
        return 0
    
    tong = 1 
    for i in range(2, (n // 2) + 1):
        if n % i == 0:
            tong += i
    return tong

def kiem_tra_hoan_thien(n):
    return tinh_tong_uoc_so(n) == n

def kiem_tra_thinh_vuong(n):
    return tinh_tong_uoc_so(n) > n

n = int(input("Nhập số nguyên dương n: "))

if n <= 0:
    print("Đây không phải là số nguyên dương.")
else:
    print(f"Tổng các ước số (không kể {n}) là: {tinh_tong_uoc_so(n)}")

    if kiem_tra_hoan_thien(n):
        print(f"-> {n} là số hoàn thiện.")
    else:
        print(f"-> {n} không phải là số hoàn thiện.")

    if kiem_tra_thinh_vuong(n):
        print(f"-> {n} là số thịnh vượng.")
    else:
        print(f"-> {n} không phải là số thịnh vượng.")