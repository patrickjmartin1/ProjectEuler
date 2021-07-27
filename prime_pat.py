from math import sqrt
from numpy import ones

def mrprime(n):
    d = int(n-1)
    y = n-1
    s = 0
    p = 0
    z  = [2,3,5,7]
    while d%2 == 0:
        d = int(d/2)
        s = s+1
    if s == 0:
        return False
    for a in z:
        m = []
        for r in range(0,s):
            m.append(pow(a,(2**r)*d,n)) #This is the BETTER version of how to raise to a power in python
        for i in range(0,len(m)):
            if (i == 0 and m[i] == 1):
                p = p+1
                break
            elif m[i] == y:
                p = p+1
                break
            elif i == len(m)-1:
                return False
    if p == 4:
        return True


# Update 4/7/19 - This is the optimal version of the code that we should use. MR2PRI worked well for PE#60, and we should use this moving forward
def mr2pri(n):
    if n == 2:
        return True
    d = int(n - 1)
    y = n - 1
    s = 0
    a = 2
    while d % 2 == 0:
        d = int(d / 2)
        s = s + 1
    if s == 0:
        return False
    m = []
    for r in range(0, s):
        m.append(pow(a,(2**r)*d,n))
    for i in range(0, len(m)):
        if (i == 0 and m[i] == 1):
            return True
        elif m[i] == y:
            return True
        elif i == len(m) - 1:
            return False


def isprime(x):
    if x == 1:
        return False
    if x == 2 or x ==3:
        return True
    else:
        for i in range(2,int(sqrt(x)+2)):
            if x%i == 0:
                return False
            elif i == int(sqrt(x)+1):
                return True

def primes(x):
    prime_list = ones(x)
    prime_list[0] = 0
    prime_list[1] = 0
    for i in range(2, x):
        if prime_list[i]:
            j = 2
            while (i * j) < x:
                prime_list[i * j] = 0
                j = j + 1
        else:
            continue
    return prime_list

def fermat_prime(n):
    a1 = 13
    a2 = 17
    first = (a1**(n-1))%n
    second = (a2**(n-1))%n
    if first == 1 and second == 1:
        x = True
    else:
        x = False
    return x

def mrfixed(n):
    ## Note: This is a more complete working version of the Miller Rabin Prime Checker
    if (n == 2) or (n == 3) or (n == 5) or (n == 7):
        return True
    d = int(n-1)
    y = n-1
    s = 0
    p = 0
    z  = [2,3,5,7]
    while d%2 == 0:
        d = int(d/2)
        s = s+1
    if s == 0:
        return False
    for a in z:
        m = []
        for r in range(0,s):
            m.append(pow(a,(2**r)*d,n)) #This is the BETTER version of how to raise to a power in python
        for i in range(0,len(m)):
            if (i == 0 and m[i] == 1):
                p = p+1
                break
            elif m[i] == y:
                p = p+1
                break
            elif i == len(m)-1:
                return False
    if p == 4:
        return

def rel_prime(x,y):
    from fractions import Fraction
    if Fraction(x,y) == 'x/y':
        return True
    else:
        return False
