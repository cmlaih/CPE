def find_smallest_multiple(n):
    """
    Find the smallest integer composed of only the digit 1 in decimal
    representation that is divisible by n.
    """
    number = 1
    length = 1

    while number % n != 0:
        number = number * 10 + 1
        length += 1

    return length

while True:
    try:
        n = int(input())
        print(find_smallest_multiple(n))
    except EOFError:
        break
