from math import sqrt, floor

def contFrac(x, k):
    cf = []
    q = floor(x)
    cf.append(q)
    x = x - q
    i = 0
    while x != 0 and i < k:
        q = floor(1 / x)
        cf.append(q)
        x = 1 / x - q
        i = i + 1
    return cf

def contFrac_eff(x):
    # A more efficient implementation of the continued fraction function
    cf = []
    q = floor(x)
    cf.append(q)
    x = x - q
    i = 0
    while x != 0 and i < 12:
        q = floor(1 / x)
        cf.append(q)
        x = 1 / x - q
        i = i + 1
    return cf

k = 1
while True:
    if k <= 51:
        print(k)
        print(contFrac_eff(sqrt(k)))
        k = k+1
    else:
        break


