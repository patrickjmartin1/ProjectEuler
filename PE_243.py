"""
Resilient Fractions

Using Sieve of Eratosthenes from:
https://www.geeksforgeeks.org/python-program-for-sieve-of-eratosthenes/

We should also think about Euler's totient function
https://en.wikipedia.org/wiki/Euler%27s_totient_function

"""
from numpy import gcd
import numpy as np
import math


def resilience(d):
    res_sum = 1
    for n in range(2, d):
        if gcd(d, n) == 1:
            res_sum += 1
    return res_sum/(d-1)


def resilience_sieve(d):
    temp = np.zeros([d+1, 1])
    temp[1] = 1
    n = 1

    while n < d:

        if temp[n] == 1:
            n += 1
            continue

        if gcd(d, n) != 1:
            mult = 1
            n_current = mult * n

            while n_current < len(temp):
                temp[n_current] = 1
                mult += 1
                n_current = mult * n

        else:
            n += 1


    temp[-1] = 0

    res_sum = d - temp.sum()

    return {'ratio': res_sum/(d-1), 'res_n': res_sum, 'res_d':(d-1)}


def SieveOfEratosthenes(n):
    # Create a boolean array "prime[0..n]" and initialize
    # all entries it as true. A value in prime[i] will
    # finally be false if i is Not a prime, else true.
    prime = [True for i in range(n + 1)]
    p = 2
    while (p * p <= n):

        # If prime[p] is not changed, then it is a prime
        if (prime[p] == True):

            # Update all multiples of p
            for i in range(p * 2, n + 1, p):
                prime[i] = False
        p += 1
    prime[0] = False
    prime[1] = False
    # Print all prime numbers
    prime_list = []
    for p in range(n + 1):
        if prime[p]:
            prime_list.append(p)
            print(p)

    return prime_list


def pi_prime(x):
    return x/(np.log(x)-1)


def prime_frac(x):
    return 1/(np.log(x)-1)


def prime_totient(n, primes):
    """
    n: Number which we want to calculate the totient of
    primes: list of primes constituting n
    return: phi(n), the number of number less than or equal to n and coprime to n
    """
    prod_temp = n
    for prime in primes:
        prod_temp *= (1 - (1/prime))

    return prod_temp


def prime_factors(n):
    # Print the number of two's that divide n
    pf = []

    if n % 2 == 0:
        pf.append(2)
        while n % 2 == 0:
            n = n / 2

    # n must be odd at this point
    # so a skip of 2 ( i = i + 2) can be used
    for i in range(3, math.ceil(math.sqrt(n+1)) + 2, 2):

        if n % i == 0:
            pf.append(i)
            # while i divides n , print i and divide n
            while n % i == 0:
                n = n / i

        if n == 1:
            break

    if n != 1:
        pf.append(n)

    return pf


if __name__ == "__main__":
    res_target = 15499 / 94744
    # res_target = 0.20
    print("Res Target: {}".format(res_target))

    d = pow(2, 3) * pow(3, 2) * pow(5, 2)
    # d = 12
    pfd = prime_factors(d)
    totient = prime_totient(d, pfd)
    ratio = totient / (d-1)
    print(d, ' ', ratio)

