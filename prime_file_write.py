from prime_pat import primes
import pickle
from timeit import default_timer
time = default_timer
t0 = time()
P = primes(int(1e8))

with open('primefile', 'wb') as fp:
    pickle.dump(P, fp)

print('All done')
t1 = time()
print(t1-t0)