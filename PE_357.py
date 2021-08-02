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


def small_factors(n):
    # return the factors of n which are less than sqrt(n)
    factors = [1]

    for i in range(2, ceil(sqrt(n))):
        if n % i == 0:
            factors.append(i)

    return factors


def main_func():
    n_max = int(1e6)
    primes = prime_sieve(int(n_max+1))

    definite_n = [1]

    possible_n = []

    for n in range(2, n_max+1, 2):
        if not primes[n+1]:
            continue
        quick_check = int(2 + (n/2))
        if not primes[quick_check]:
            continue

        if primes[int(n/2)]:
            definite_n.append(n)
            continue

        # Let's quick check 3
        if n % 3 == 0:
            if not primes[int(n / 3) + 3]:
                continue

        # Let's quick check 5
        if n % 5 == 0:
            if not primes[int(n / 5) + 5]:
                continue

        possible_n.append(n)

    for n in possible_n:
        n_factors = small_factors(n)
        valid = True
        # check if this holds
        for factor in n_factors:
            if not primes[int(factor + (n / factor))]:
                possible_n.remove(n)
                valid = False
                break
        if valid:
            definite_n.append(n)

    print(definite_n)
    print(len(definite_n))
    print("sum: {}".format(sum(definite_n)))


if __name__ == "__main__":
    main_func()

