while True:
    try:
        n = int(input())  # Number of books
        prices = list(map(int, input().split()))  # Prices of the books
        money = int(input())  # Total money available

        prices.sort()  # Sort the prices for binary search

        i, j = 0, n - 1
        best_i, best_j = 0, 0

        while i < j:
            if prices[i] + prices[j] == money:
                best_i, best_j = i, j
                i += 1
                j -= 1
            elif prices[i] + prices[j] < money:
                i += 1
            else:
                j -= 1

        print(f"Peter should buy books whose prices are {prices[best_i]} and {prices[best_j]}.")
        print()  # Blank line between two cases

        input()  # Read the blank line between two consecutive test cases

    except EOFError:
        break  # Exit the loop at the end of the input
