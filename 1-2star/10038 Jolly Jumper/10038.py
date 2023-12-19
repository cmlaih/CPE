def is_jolly_jumper(numbers):
    n = len(numbers)
    if n == 1:
        return True  # A single number is trivially a Jolly Jumper

    differences = set(abs(numbers[i] - numbers[i-1]) for i in range(1, n))

    return all(diff in differences for diff in range(1, n))

while True:
    try:
        numbers = list(map(int, input().split()))[1:]  # First element is the length, so skip it
        if is_jolly_jumper(numbers):
            print("Jolly")
        else:
            print("Not jolly")
    except EOFError:
        break