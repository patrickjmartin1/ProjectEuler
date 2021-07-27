import numpy as np
from prime_pat import isprime


def prime_concat(a, b):
    x = int(str(a) + str(b))
    y = int(str(b) + str(a))
    return x, y

search_max = 1000
Prime_Values = np.array([[1,2,3], [4,5,6]])
print(Prime_Values[0][2])
print(np.sum(Prime_Values, axis=1))


