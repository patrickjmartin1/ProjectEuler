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
    pd = []
    count = 0
    for i in range(1,limit):
        if pri[i]:
            pd.append(i)
    L = len(pd)
    cons = zeros(limit**4)
    for i in range(1,L-3):
        for j in range(i+1,L-2):
            for k in range(j+1,L-1):
                for l in range(k+1,L):
                    q = pd[i]*pd[j]*pd[k]*pd[l]
                    cons[q]=1
    for i in range(1,len(cons)):
        if cons[i]:
            count = count+1
            if count == n:
                return (i-n+1)
        else:
            count = 0



print(connum(4,100))
t1 = default_timer()
print(t1-t0)

#Note this runs too slow, we're going to optimize
