from pat_lib import pandigital
from numpy import zeros
from prime_pat import primes
from timeit import default_timer
t0 = default_timer()
maxval = 99999
maxrep = 0
nmax = 0
for i in range(1,maxval):
    rep = ''
    n=1
    while len(rep) < 9:
        rep = rep+str(i*n)
        n=n+1
    if pandigital(rep,9):
        if int(rep)>maxrep:
            maxrep = int(rep)
            nmax = n-1


t1 = default_timer()
print(maxrep,nmax)
print(t1-t0)






