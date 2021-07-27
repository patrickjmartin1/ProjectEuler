import time
t0 = time.time()
import math
from math import sqrt
from numpy import ones

y = 100000

def primes(x):
    prime_list= ones((x,), dtype=int)
    prime_list[:2] = 0
    for i in range(2,int(x/2)+1):
        j = 2
        while i*j<x:
            prime_list[i*j] = 0
            j = j+1
            continue
    return prime_list
print(primes(y))
t1 = time.time()
total1 = t1-t0
print('execution time 1: ', total1)


t2 = time.time()

def primes2(x):
    prime_list2 = ones((x,), dtype=int)
    prime_list2[:2] = 0
    for i in range(2,x):
        if prime_list2[i]:
            j = 2
            while (i*j)<x:
                prime_list2[i*j]=0
                j=j+1
        else:
            continue
    return prime_list2
print(primes2(y))
t3 = time.time()
total2 = t3 - t2
print('execution time 2: ', total2)

print(primes2(100)[79])