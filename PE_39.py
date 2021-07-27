from timeit import default_timer
t0 = default_timer()
countmax = 0
pmax = 0
for p in range(3,1001):
    print(p)
    count = 0
    for s1 in range(1,p):
        for s2 in range(s1,p):
            s3 = p -(s1+s2)
            if s3**2 < (s1**2) + (s2**2):
                break
            if s3**2 == (s1**2) + (s2**2):
                count = count+1
            if count >countmax:
                countmax = count
                pmax = p

print(countmax, pmax)
t1 = default_timer()
print(t1-t0)