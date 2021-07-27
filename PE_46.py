from prime_pat import primes
from math import sqrt
from timeit import default_timer
t0 = default_timer()


def gbcon(m):
    maxn = m
    prime = primes(maxn)
    for i in range(33,maxn,2):
        if prime[i]:
            continue
        else:
            for j in range(1,i,2):
                if prime[j]:
                    t = sqrt((i-j)/2)
                    if t == int(t):
                        break
                    elif j == (i-1):
                        print('winner')
                        print(i)
                        return i
                    else:
                        continue
        if i == maxn-2:
            print('Sorry go higher')
            return 0
        else:
            continue
print(gbcon(10001))
t1 = default_timer()
print(t1-t0)