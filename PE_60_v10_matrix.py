import numpy as np
from prime_pat import isprime


def prime_concat(a, b):
    x = int(str(a) + str(b))
    y = int(str(b) + str(a))
    return x, y

search_max = 1000
Prime_Values = np.zeros((search_max, search_max), 'b')

for i in range(1, search_max):
    if not isprime(i):
        continue
    else:
        for j in range(i, search_max):
            if isprime(j):
                [x, y] = prime_concat(i, j)
                if isprime(x) and isprime(y):
                    Prime_Values[i][j] = 1
                else:
                    continue

Prime_Rows = np.sum(Prime_Values, axis=1)
print(Prime_Values[3][673])
print(Prime_Rows)
print(len(Prime_Rows))


for h in range(1, search_max):
    if Prime_Rows[h] >= 4:
        for i in range(h+1, search_max):
            if Prime_Values[h][i]:
                for j in range(i+1, search_max):
                    if Prime_Values[h][j] and Prime_Values[i][j]:
                        for k in range(j+1, search_max):
                            if Prime_Values[h][k] and Prime_Values[i][k] and Prime_Values[j][k]:
                                for m in range(k+1, search_max):
                                    if Prime_Values[h][m] \
                                            and Prime_Values[i][m] \
                                            and Prime_Values[j][m] \
                                            and Prime_Values[k][m]:
                                        NUMS = [h, i, j, k, m]
                                        print(NUMS, sum(NUMS))
                                        raise Exception('Found the Answer!')

                                    else:
                                        continue
                            else:
                                continue
                    else:
                        continue
            else:
                continue
    elif h == search_max - 1:
        print('All Done')

    else:
        continue



