from pat_lib import pandigital
from prime_pat import mrprime, primes
from timeit import default_timer
t0 = default_timer()
maxval = 10000000
hiprime = 0
for i in range(2141,maxval,2):
    if pandigital(str(i), len(str(i))):
        if mrprime(i):
            print(i)
            hiprime = i


t1 = default_timer()
print(hiprime)
print(t1-t0)






