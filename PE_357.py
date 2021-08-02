"""
Prime Generating Integers

Rules:
    - No odd numbers can count towards the sum (sum will be even - not prime)
    - No even numbers one less than non primes
    - Must be even numbers, therefore 2 + n/2 must be prime

We need only search through the even numbers, and we only need to vigorously check a few


"""

from prime_sieve import prime_sieve
from math import sqrt, ceil


def div_by_x(n, x):
    # return a boolean list of the numbers which are divisible by x
    div = [False for i in range(n + 1)]
    for i in range(x, n, x):
        div[i] = True
    return div


def small_factors(n):
    # return the factors of n which are less than sqrt(n)
    factors = [1]

    for i in range(2, ceil(sqrt(n))+1):
        if n % i == 0:
            factors.append(i)

    return factors


def main_func():
    n_max = int(1e8)
    div_by_3 = div_by_x(n_max + 1, 3)
    div_by_5 = div_by_x(n_max + 1, 5)
    div_by_7 = div_by_x(n_max + 1, 7)
    div_by_11 = div_by_x(n_max + 1, 11)
    div_by_13 = div_by_x(n_max + 1, 13)
    div_by_17 = div_by_x(n_max + 1, 17)
    primes = prime_sieve(int(n_max+1))

    definite_n = [1]

    possible_n = []

    # Build list of definite and possible n values
    for n in range(2, n_max+1, 4):
        if not primes[n+1]:
            continue

        # We know the number is divisible by two
        if not primes[int(n/2) + 2]:
            continue

        if primes[int(n/2)]:
            definite_n.append(n)
            continue

        # Check most lowest prime numbers
        if div_by_3[n] and not primes[int(n / 3) + 3]:
            continue

        if div_by_5[n] and not primes[int(n / 5) + 5]:
            continue

        if div_by_7[n] and not primes[int(n / 7) + 7]:
            continue

        if div_by_11[n] and not primes[int(n / 11) + 11]:
            continue

        if div_by_13[n] and not primes[int(n / 13) + 13]:
            continue

        if div_by_17[n] and not primes[int(n / 17) + 17]:
            continue

        possible_n.append(n)

    # verify possible n values, and append them to definite n values
    for n in possible_n:
        n_factors = small_factors(n)
        valid = True
        # check if this holds
        for factor in n_factors:
            if not primes[factor + int(n / factor)]:
                valid = False
                break
        if valid:
            definite_n.append(n)

    definite_n.sort()
    print('\n\n')
    print(definite_n)
    print(len(definite_n))
    print("sum: {}".format(sum(definite_n)))


if __name__ == "__main__":
    main_func()

""" 
This produces the correct sum of 1739023853137, list length of 39627
"""
