def count_unique_prime_factors(n):
    """
    Count the number of unique prime factors of a given number n.
    """
    unique_factors = 0
    factor = 2

    while factor * factor <= n:
        if n % factor == 0:
            unique_factors += 1
            while n % factor == 0:
                n //= factor
        factor += 1

    if n > 1:
        unique_factors += 1

    return unique_factors
while True:
  n = int(input())
  if n == 0:
    break
  else:
    print("{} : {}".format(n, count_unique_prime_factors(n)))
