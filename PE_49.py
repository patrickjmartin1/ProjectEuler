from prime_pat import primes
from pat_lib import pup
from timeit import default_timer
t0 = default_timer()
p = primes(10000)
def pp():
    for i in range(1488,10000):
        if p[i]:
            x = i
            r = [x]
            r2 = []
            while pup(x) is not False:
                x = pup(x)
                r.append(x)
            for k in r:
                if p[k]:
                    r2.append(k)
            if len(r2)<=2:
                for m in r2:
                    p[m]=0
            for j in range(0,len(r2)-2):
                for k in range(j+1,len(r2)-1):
                    for l in range(k+1,len(r2)):
                        a = r2[l] - r2[k]
                        b = r2[k] - r2[j]
                        if a == b:
                            return(str(r2[j])+str(r2[k])+str(r2[l]))
t1 = default_timer()
print(pp())
print(t1-t0)