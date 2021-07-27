from math import sqrt
tot_max = 0

def prime_factors(x):
    PFs = []
    i = 2
    while x != 1:
        if x % i == 0:
            PFs.append(i)
            x = x/i
            continue
        else:
            i = i + 1
    if PFs == []:
        PFs.append(x)
    return list(set(PFs))

def coprime(a,b):
    for i in a:
        if i in b:
            return False
    return True


# print(coprime(prime_factors(11*11*11*13), prime_factors(13*13)))

T_max = 0
n_best = 0
n_max = 12
for i in range(2,n_max):
    print(i)
    a = prime_factors(i)
    n = [1]
    for j in range(2,i):
        b = prime_factors(j)
        if coprime(a, b):
            n.append(j)
    T = i/len(n)
    print(T)
    if T > T_max:
        T_max = T
        n_best = i

print(n_best)
print(T_max)

