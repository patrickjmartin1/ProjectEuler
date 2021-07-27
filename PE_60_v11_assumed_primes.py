import numpy as np
from prime_pat import isprime


def prime_concat(a, b):
    x = int(str(a) + str(b))
    y = int(str(b) + str(a))
    return x, y

starter_primes = [3, 7, 13]

for i in starter_primes:
    for j in starter_primes:
        if j ==i:
            continue

        [x, y] = prime_concat(i, j)
        print(i, j)
        print(isprime(x), isprime(y))