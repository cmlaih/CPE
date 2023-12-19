def is_happy_number(n):
    """
    Determine if a given number is a happy number.
    """
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = sum(int(digit) ** 2 for digit in str(n))
    return n == 1

def main():
    T = int(input())
    for case in range(1, T + 1):
        n = int(input())
        if is_happy_number(n):
            print(f"Case #{case}: {n} is a Happy number.")
        else:
            print(f"Case #{case}: {n} is an Unhappy number.")
if __name__ == "__main__":
    main()
