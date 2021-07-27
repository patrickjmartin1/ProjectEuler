from prime_pat import primes
from numpy import zeros
from timeit import default_timer
t0 = default_timer()

def cons(x,limit):
    p = primes(limit)
    cons = zeros(limit)
    for i in range(1,len(p)):
        if p[i]==1:
            j = 1
            while j*i<limit:
                cons[j*i] = cons[j*i]+1
                j = j+1
    cts=0
    for i in range(1,len(cons)):
        if cons[i]==4:
            cts = cts+1
            if cts == x:
                return (i-x+1)
        else:
            cts = 0

print(cons(4,1000000))
t1 = default_timer()
print(t1-t0)


