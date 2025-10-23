#Câu 8: Tách lấy tên bài hát
import os

def LayTenFileDayDu(path):
    return os.path.basename(path)

def LayTenBaiHatGoc(path):
    ten_file = os.path.basename(path)
    ten_bai, _ = os.path.splitext(ten_file)
    return ten_bai

path_input = "d:\\music\\muabui.mp3"
print(f"Đường dẫn ví dụ: {path_input}")

print(f"Lấy ra muabui.mp3: {LayTenFileDayDu(path_input)}")
print(f"Lấy ra muabui: {LayTenBaiHatGoc(path_input)}")

path_input_2 = input("\nNhập đường dẫn của bạn: ")
if path_input_2:
    print(f"Tên file đầy đủ: {LayTenFileDayDu(path_input_2)}")
    print(f"Tên bài hát gốc: {LayTenBaiHatGoc(path_input_2)}")