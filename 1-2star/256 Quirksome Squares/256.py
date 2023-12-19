def find_special_numbers():
    ans = {k: [] for k in range(2, 9, 2)}  # Dictionary to store results for 2, 4, 6, 8 digits
    div = [10, 100, 1000, 10000]

    for i in range(10000):
        square = i * i
        for j in range(4):
            if i < div[j]:
                x = square // div[j] + square % div[j]
                if x == i:
                    ans[j * 2 + 2].append(square)

    return ans

def display_special_numbers(ans, n):
    idx = n // 2 - 1
    for num in ans[n]:
        print(f"{num:0{n}d}")

def main():
    ans = find_special_numbers()
    while True:
        try:
            n = int(input("Enter the number of digits (2, 4, 6, or 8): "))
            if n in ans:
                display_special_numbers(ans, n)
            else:
                print("Please enter 2, 4, 6, or 8.")
        except EOFError:
            break

if __name__ == "__main__":
    main()
