from numpy import zeros
from math import sqrt
from timeit import default_timer
t0 = default_timer()

def gonal(limit):

    p = []
    t = []
    h = []

    n = 1
    d = 4
    while n < limit:
        p.append(n)
        n = n + d
        d = d+3

    n = 1
    d = 2
    while n<limit:
        t.append(n)
        n = n+d
        d = d+1

    n = 1
    d = 5
    while n<limit:
        h.append(n)
        n=n+d
        d = d+4

    for i in h[144:]:
        tn = int(sqrt(8*i)/2)
        pn = int(sqrt(24*i)/6)
        if i in p[pn-2:pn+2]:
            if i in t[tn-2:tn+2]:
                return i


print(gonal(10000000000))
t1 = default_timer()
print(t1-t0)


