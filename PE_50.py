from prime_pat import primes
from timeit import default_timer
t0 = default_timer()
def conprime(x):
    P = primes(int(x))
    longest = 0
    maxprime = 0
    for i in range(1,x):
        if P[i]:
            cur_sum = i
            length = 1
            for j in range(i+2,x):
                if P[j]:
                    cur_sum = cur_sum+j
                    if cur_sum>=x:
                        break
                    length = length+1
                    if P[cur_sum]:
                        if length > longest:
                            longest = length
                            maxprime = cur_sum
    return(maxprime, longest)
print(conprime(1000000))
t1 = default_timer()
print(t1-t0)