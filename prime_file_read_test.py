import pickle
from timeit import default_timer
from prime_pat import primes
time = default_timer

t0 = time()

with open ('primefile', 'rb') as fp:
    prime_list = pickle.load(fp)

t1 = time()

print(t1-t0)
prime_list2 = primes(int(1e6))

t2 = time()

print(t2-t1)
