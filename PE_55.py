from timeit import default_timer as time
t0 = time()
from pat_lib import reverse
count = 0
for i in range(1,10001):
    x = i
    lychrel = True
    iteration = 0
    while lychrel == True:
        y = reverse(x)
        z = x+y
        if z == reverse(z):
            lychrel = False
        else:
            x = z
            iteration = iteration + 1
        if iteration == 50:
            count = count+1
            lychrel = False
t1 = time()
print(count)
print(t1-t0)

