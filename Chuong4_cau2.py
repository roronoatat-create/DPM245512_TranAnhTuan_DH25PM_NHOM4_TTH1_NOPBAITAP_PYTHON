#Câu 2: Viết Hàm để chơi Game Đoán Số
from random import randrange

while True:
    somay = randrange(1, 101)
    solandoan = 0
    win = False
    
    while solandoan < 7:
        solandoan += 1
        # Sửa lại câu prompt cho đúng (trong hình bị gõ nhầm)
        songuoi = int(input(f"Đoán lần thứ {solandoan} [1..100]: "))

        if somay == songuoi:
            print("Chúc mừng bạn đoán đúng, số máy là =", somay)
            win = True
            break
        elif somay > songuoi:
            print("Bạn đoán sai, số máy > số bạn")
        else: # somay < songuoi
            print("Bạn đoán sai, số máy < số bạn")

    if win == False:
        print("GAME OVER!, số máy =", somay)
        
    hoi = input("Tiếp không? (nhập 'k' để dừng): ")
    if hoi == "k":
        break

print("Cám ơn bạn đã chơi Game!")