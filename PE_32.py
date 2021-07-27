from numpy import zeros
from timeit import default_timer
t0 = default_timer()
products = zeros(1000000)
for i in range(1,1000):
    for j in range(i,10000):
        k = i*j
        stringrep = str(i)+str(j) + str(k)
        count = 0
        for a in range(1,10):
            if len(stringrep)!=9:
                break
            if str(a) not in stringrep:
                break
            elif a == 9:
                products[k] = 1
tsum = 0
for i in range(1,len(products)):
    if products[i]:
        print(products[i],i)
        tsum = tsum + i

print(tsum)
t1 = default_timer()
print(t1-t0)