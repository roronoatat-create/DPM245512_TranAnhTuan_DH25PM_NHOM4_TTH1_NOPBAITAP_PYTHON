#Câu 5: Xử lý chuỗi với các hàm cơ bản
s = input("Nhập vào 1 chuỗi: ")

hoa = 0
thuong = 0
so = 0
kytudacbiet = 0
khoangtrang = 0
nguyenam = 0
phuam = 0

ds_nguyenam = "aeiouAEIOU"

for ky_tu in s:
    if ky_tu.isupper():
        hoa += 1
        if ky_tu in ds_nguyenam:
            nguyenam += 1
        else:
            phuam += 1
    elif ky_tu.islower():
        thuong += 1
        if ky_tu in ds_nguyenam:
            nguyenam += 1
        else:
            phuam += 1
    elif ky_tu.isdigit():
        so += 1
    elif ky_tu.isspace():
        khoangtrang += 1
    else:
        kytudacbiet += 1

print(f"Bao nhiêu chữ IN HOA: {hoa}")
print(f"Bao nhiêu chữ in thường: {thuong}")
print(f"Bao nhiêu chữ là chữ số: {so}")
print(f"Bao nhiêu chữ là ký tự đặc biệt: {kytudacbiet}")
print(f"Bao nhiêu chữ là khoảng trắng: {khoangtrang}")
print(f"Bao nhiêu chữ là Nguyên Âm: {nguyenam}")
print(f"Bao nhiêu chữ là Phụ âm: {phuam}")