prime_numbers = [x for x in range(2, 1001) if all(x % x2 for x2 in range(2, x))]
