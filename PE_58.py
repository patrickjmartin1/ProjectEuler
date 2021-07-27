from timeit import default_timer as time
t0 = time()
from prime_pat import isprime

sidelen = 3
currentnum = 1
diags = [1]
stopnum = 1000000000
prime_count = 0
while currentnum<stopnum:
    ind = 0
    while ind <4:
        stepsize = sidelen-1
        currentnum = currentnum+stepsize
        ind = ind + 1
        diags.append(currentnum)

    for i in diags[-4:]:
        if isprime(i):
            prime_count = prime_count+1
    total = len(diags)
    if (prime_count/total) < 0.1:
        print(sidelen)
        break
    else:
        sidelen = sidelen + 2
        continue

if currentnum >= stopnum:
    print('We have reached the end of our limit')
t1 = time()
print(t1-t0)