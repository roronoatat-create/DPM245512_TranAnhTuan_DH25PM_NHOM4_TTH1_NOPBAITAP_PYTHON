#Câu 7: Tối ưu chuỗi danh từ
def ToiUuChuoiDanhTu(s):
    s_tam = s.strip()
    s_tam = ' '.join(s_tam.split())
    s_ketqua = s_tam.title()
    return s_ketqua

s_input = " Trần duY thAnh "
s_output = ToiUuChuoiDanhTu(s_input)

print(f"Input: '{s_input}'")
print(f"Output: '{s_output}'")

s_input_2 = input("\nNhập chuỗi của bạn để tối ưu: ")
print(f"Output: '{ToiUuChuoiDanhTu(s_input_2)}'")