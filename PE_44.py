from numpy import zeros
from timeit import default_timer
t0 = default_timer()

def pent(limit):
    n = 1
    d = 4
    p = zeros(limit)
    pns = []
    while n < limit:
        pns.append(n)
        p[n] = 1
        n = n + d
        d = d+3
    for i in range(0,len(pns)-1):
        for j in range(i+1,len(pns)):
            x = pns[i] + pns[j]
            if x>limit:
                break
            if p[pns[j]-pns[i]] and p[x]:
                return pns[j],pns[i],pns[j] - pns[i]
print(pent(10000000))
t1 = default_timer()
print(t1-t0)


