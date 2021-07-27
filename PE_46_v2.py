from prime_pat import primes
from math import sqrt
from numpy import zeros
from timeit import default_timer
t0 = default_timer()

def gbcon(m):
    maxn = m
    prime = primes(maxn)
    conjecture = prime
    for q in range(0,maxn,2):
        conjecture[q]=1
    conjecture[0:2] = 1
    squares = []
    for i in range(1,int(sqrt((maxn-2)/2))+1):
        squares.append(2*(i**2))
    for x in range(1,maxn):
        if conjecture[x] == 0:
            for y in squares:
                rem=x-y
                if rem<0:
                    return x
                if prime[rem]:
                    break
                else:
                    continue
        if x == maxn-1:
            print('sorry go higher')
            return 0

print(gbcon(1000001))
t1 = default_timer()
print(t1-t0)
