## PE #60 - Final, working solution. The primes are 13, 5197, 5701, 6733, 8389, with a sum of 26033.
## Takes approximately 90 seconds on my computer

from prime_pat import isprime, mr2pri
import pandas as pd
from timeit import default_timer as time

t1 = time()


def prime_concat(a, b):
    x = int(str(a) + str(b))
    y = int(str(b) + str(a))
    if mr2pri(x) and mr2pri(y):
        return True
    else:
        return False

A = prime_concat(3, 7)

primes = []

for i in range(1, 10000):
    if isprime(i):
        primes.append(i)
print(len(primes))

prime_df = pd.DataFrame(index = primes, columns = primes)

for i in range(0, len(primes)):
    for j in range(i, len(primes)):
        if prime_concat(primes[i], primes[j]):
            prime_df[primes[i]][primes[j]] = 1
            continue
        else:
            prime_df[primes[i]][primes[j]] = 0
            continue

prime_df_sum = prime_df.sum(axis = 0, skipna = True)

solved = False
while not solved:
    for h in range(0, len(primes)):
        h_prime = primes[h]
        if prime_df_sum[h_prime] < 4:
            continue
        elif h == len(primes) - 1:
            print('All Done')
            break
        else:
            for i in range(h, len(primes)):
                i_prime = primes[i]
                if prime_df[h_prime][i_prime]:
                    for j in range(i, len(primes)):
                        j_prime = primes[j]
                        if prime_df[h_prime][j_prime] and prime_df[i_prime][j_prime]:
                            for k in range(j, len(primes)):
                                k_prime = primes[k]
                                if prime_df[h_prime][k_prime] and prime_df[i_prime][k_prime] and prime_df[j_prime][k_prime]:
                                    for m in range(k, len(primes)):
                                        m_prime = primes[m]
                                        if prime_df[h_prime][m_prime] and prime_df[i_prime][m_prime] and prime_df[j_prime][m_prime] and prime_df[k_prime][m_prime]:
                                            NUMS = [h_prime, i_prime, j_prime, k_prime, m_prime]
                                            print(NUMS, sum(NUMS))
                                            solved = True
                                            break
                                        else:
                                            continue
                                elif solved:
                                    break
                                else:
                                    continue
                        elif solved:
                            break
                        else:
                            continue
                elif solved:
                    break
                else:
                    continue

t2 = time()

print("Total Time:")
print(t2-t1)

