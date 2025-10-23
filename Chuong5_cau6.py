#Câu 6: Trích lọc số âm trong chuỗi
import re

def NegativeNumberInStrings(s):
    so_am = re.findall(r'-\d+', s)
    
    print(f"Các số âm tìm thấy trong chuỗi:")
    if not so_am:
        print("Không tìm thấy số âm nào.")
    else:
        for so in so_am:
            print(so)

s_input = input("Nhập vào một chuỗi (ví dụ: abc-5xyz-12k9l--p): ")
NegativeNumberInStrings(s_input)