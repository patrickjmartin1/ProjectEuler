from pat_lib import lrtrunc, rltrunc
from numpy import zeros
from prime_pat import primes
from timeit import default_timer
t0 = default_timer()
maxval = 1000000
prime_list = primes(maxval)
truncates = zeros(maxval)
isum = 0
for i in range(11,maxval,2):
    if prime_list[i]:
        m = i
        n = i
        while len(str(m))>0:
            m = lrtrunc(m)
            n = rltrunc(n)
            if prime_list[m] and prime_list[n] and len(str(m))==1:
                truncates[i] = 1
                isum = isum+i
                print(i)
                break
            elif prime_list[m] and prime_list[n]:
                continue
            else:
                break
t1 = default_timer()
print(isum)
print(t1-t0)
PE_41.py





