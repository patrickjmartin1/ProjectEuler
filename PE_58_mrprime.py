from timeit import default_timer as time
t0 = time()
from prime_pat import mrfixed
import numpy as np
import matplotlib.pyplot as plt

sidelen = 3
currentnum = 1
diags = [1]
stopnum = 1000000000
prime_count = 0
fracs = []
while currentnum<stopnum:
    ind = 0
    while ind <4:
        stepsize = sidelen-1
        currentnum = currentnum+stepsize
        ind = ind + 1
        diags.append(currentnum)

    for i in diags[-4:]:
        if mrfixed(i):
            prime_count = prime_count+1
    total = len(diags)
    frac = (prime_count/total)
    fracs.append(frac)
    if frac < 0.1:
        print(sidelen)
        print(currentnum)
        break
    else:
        sidelen = sidelen + 2
        continue

if currentnum >= stopnum:
    print('We have reached the end of our limit')
t1 = time()
print(t1-t0)
x = np.linspace(0,len(fracs),len(fracs))
plt.plot(x,fracs)
plt.show()