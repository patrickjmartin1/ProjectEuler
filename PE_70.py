from sympy.ntheory import totient
import time


# Python program to print all primes smaller than or equal to
# n using Sieve of Eratosthenes


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
    for p in range(n + 1):
        if prime[p]:
            print
            p,  # Use print(p) for python 3

    return prime


def getSortedNumber(n):
    # Convert to equivalent string
    number = str(n)

    # Sort the string
    number = ''.join(sorted(number))

    # Convert to equivalent integer
    number = int(number)

    # Return the integer
    return number


# driver program
if __name__ == '__main__':
    n = int(1e5)
    print("Following are the prime numbers smaller than or equal to {}".format(n))
    # Use print("than or equal to", n) for Python 3
    siv = SieveOfEratosthenes(n)
    # print(siv)
    print(siv[11])

    for indx in range(len(siv)-1, 0-1, -1):
        # If it's a prime number
        if siv[indx]:

            # calculate the totient
            t = totient(indx)
            n_sorted = getSortedNumber(indx)
            phi_sorted = getSortedNumber(t)

            if n_sorted == phi_sorted:
                print('Permutation!')
                print("n: {}, phi: {}".format(n_sorted, phi_sorted))
                print('{} is prime'.format(indx))
                print('totient: {}'.format(t))
