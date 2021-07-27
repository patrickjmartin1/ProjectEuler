from prime_pat import isprime, primes
from math import sqrt
from numpy import zeros
from timeit import default_timer
t0 = default_timer()

def dpf(x,limit,pri): #Distinct prime factor function
    fc = 0
    for i in range(limit):
        if pri[i]:
            #Try to divide by i
            if x%i==0:
                fc = fc+1
                while x%i == 0:
                    x=x/i
        if x == 1:
            break
    return fc

def connum(n,limit):
    pri = primes(limit)
    cons = []
    for i in range(1,limit):
        if dpf(i,limit,pri) >= n:
            cons.append(1)
            if len(cons)==n:
                return (i-n+1)
        else:
            cons = []


print(connum(3,10000))
t1 = default_timer()
print(t1-t0)

#Note this runs too slow, we're going to optimize
