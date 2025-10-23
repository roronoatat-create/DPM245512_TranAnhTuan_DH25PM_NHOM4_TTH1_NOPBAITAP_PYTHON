#Câu 5: Viết hàm đệ qui Fibonacci
def fibonacci(n):
    if n <= 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

def listfibo(n):
    print(f"\nDãy số Fibonacci từ 1 tới {n} là:")
    for i in range(1, n + 1):
        print(fibonacci(i), end='\t')
    print()

N_test = 9

print("--- Chương trình tính dãy số Fibonacci ---")

print(f"Số Fibonacci tại vị trí N={N_test}: {fibonacci(N_test)}")

listfibo(N_test)