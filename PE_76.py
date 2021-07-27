"""
We are basically solving the partition function

https://en.wikipedia.org/wiki/Partition_(number_theory)

Name sounds similar to something we handled in statistical mechanics...?
"""
from math import sqrt, ceil, floor

#    0  1  2  3  4  5   6
# p = [1, 1, 2, 3, 5, 7, 10]
p = [1]

n_max = 100
n = 1

# Calculate all
while n <= n_max:
    k_min = ceil(-(sqrt(24*n + 1) - 1) / 6)
    k_max = floor((sqrt(24*n + 1) + 1) / 6)
    print('K min: {}, K max: {}'.format(k_min, k_max))

    p_current = 0
    for k in range(k_min, k_max+1):
        p_index = int(n - k*(3*k - 1)/2)
        print(k)
        print(p_index)
        print('\n')
        if p_index == n:
            continue
        partial_sum = pow(-1, k+1) * p[p_index]
        p_current += partial_sum

    p.insert(n, p_current)
    n += 1

print(p)

p_100 = int(p[100] - 1)

print('p[100]-1: {}'.format(p_100))