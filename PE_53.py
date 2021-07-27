from timeit import default_timer as time
from math import factorial
t0 = time()

def Cnr(n,r):
    c_val = int( factorial(n)/(factorial(r)*factorial(n-r)))
    return c_val
count = 0
for n in range(23,101):
    for r in range(1,n+1):
        if Cnr(n,r)>int(1e6):
            count  = count+1
t1 = time()
print(count)
print(t1-t0)