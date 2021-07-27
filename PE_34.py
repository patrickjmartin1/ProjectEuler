# Only need to look at numbers up to 5e6
from timeit import default_timer
t0 = default_timer()
from math import factorial
global totalsum
totalsum = 0
for i in range(3,5000000):
    x = str(i)
    l = 0
    for j in x:
        l = l + factorial(int(j))
    if l == i:
        totalsum = totalsum+l
        print(totalsum)
    else:
        continue

print(totalsum)
t1 = default_timer()
print(t1-t0)