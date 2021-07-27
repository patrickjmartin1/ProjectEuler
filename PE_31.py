from timeit import default_timer
from math import ceil
t0 = default_timer()
waystocount = 1
csum1= csum2= csum3 = csum4=csum5=csum6 = 0
for L1 in range(2,-1,-1):
    csum1 = (100*L1)
    for p50 in range(int(ceil((200-csum1)/50)),-1,-1):
        csum2 = csum1+(50*p50)
        for p20 in range(int(ceil((200-csum2)/20)),-1,-1):
            csum3 = csum2+(20*p20)
            for p10 in range(int(ceil((200-csum3)/10)),-1,-1):
                csum4 = csum3 +(10*p10)
                for p5 in range(int(ceil((200-csum4)/5)),-1,-1):
                    csum5 = csum4 + (5*p5)
                    for p2 in range(int(ceil((200-csum5)/2)),-1,-1):
                        csum6 = csum5 + (2*p2)
                        for p1 in range(int(ceil(200-csum6)),-1,-1):
                            tsum = csum6+p1
                            if tsum == 200:
                                waystocount = waystocount+1

t1 = default_timer()
print(waystocount)
print(t1-t0)