#Câu 12: Hàm oscillate
def oscillate(start, stop):
    for n in range(start, stop):
        yield n
        yield -n

for n in oscillate(-3, 5):
    print(n, end=' ')
print()