#This version will remove any of the triangle numbers parts, they are redundant with hex numbers
from math import sqrt
from timeit import default_timer
t0 = default_timer()

def gonal(limit):
    p = []
    h = []
    n = 1
    d = 4
    while n < limit:
        p.append(n)
        n = n + d
        d = d+3
    n = 1
    d = 5
    while n<limit:
        h.append(n)
        n=n+d
        d = d+4
    for i in h[144:]:
        pn = int(sqrt(24*i)/6)
        if i in p[pn-2:pn+2]:
            return i
print(gonal(10000000000))
t1 = default_timer()
print(t1-t0)


