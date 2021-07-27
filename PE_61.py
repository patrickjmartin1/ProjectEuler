from timeit import default_timer as tic
from itertools import permutations
from copy import deepcopy
import traceback
import sys


t1 = tic()

D3 = {}
D4 = {}
D5 = {}
D6 = {}
D7 = {}
D8 = {}

# soln_set = [4186, 8614, 1426, 2628, 2821, 2116, 1653, 5356, 5688, 8855, 5565, 6533, 3364, 6441]
# print(sum(soln_set))
# print(soln_set)
# print(set(soln_set))
#
# exit()

soln_set = [2512, 1281, 8128, 2882, 8256, 5625]
print(sum(soln_set))
print(soln_set)
print(set(soln_set))

exit()

def cyclic_match(A, B, C):
    A_vals = C.values()
    for k in A_vals:
        try:
            for a in k:
                for b in B:
                    if (str(a)[2:] == str(b)[:2]):
                        A[a].append(b)
        except TypeError:
            for b in B:
                if (str(k)[2:] == str(b)[:2]):
                    A[k].append(b)
        # except KeyError:
        #     exc_info = sys.exc_info()
        #     traceback.print_exception(*exc_info)
        #     print(A)
        #     print(a)
        #     print(type(a))
        #     exit(1)
    A_temp = deepcopy(A)
    for key, val in A_temp.items():
        if val == []:
            del A[key]
        elif type(val) == int:
            continue
        elif type(val) == list:
            A[key] = list(set(val))
    return A

def cyclic_match_2(A, B):
    for i in A:
        try:
            B[A[i]]
        except KeyError:
            A[i] = []
        except TypeError:
            for j in A[i]:
                try:
                    B[j]
                except KeyError:
                    A[i].remove(j)
    A = {key: list(set(val)) for key, val in A.items() if val != []}
    return A

# First let's go ahead and generate the polygonal numbers, and put them in their own arrays

# Triangle
for n in range(0, 200):
    T_n = int(n * (n+1) / 2)
    if T_n < 1000:
        continue
    elif T_n < 10000:
        D3[T_n] = []
    else:
        break

# Square
for n in range(0, 200):
    T_n = n ** 2
    if T_n < 1000:
        continue
    elif T_n < 10000:
        D4[T_n] = []
    else:
        break

# Pentagonal
for n in range(0, 200):
    T_n = int(n * (3*n - 1) / 2)
    if T_n < 1000:
        continue
    elif T_n < 10000:
        D5[T_n] = []
    else:
        break

# Hexagonal
for n in range(0, 200):
    T_n = n * (2*n - 1)
    if T_n < 1000:
        continue
    elif T_n < 10000:
        D6[T_n] = []
    else:
        break

# Heptagonal
for n in range(0, 200):
    T_n = int( n * (5*n - 3) / 2)
    if T_n < 1000:
        continue
    elif T_n < 10000:
        D7[T_n] = []
    else:
        break

# Octagonal
for n in range(0, 200):
    T_n = n * (3*n - 2)
    if T_n < 1000:
        continue
    elif T_n < 10000:
        D8[T_n] = []
    else:
        break

t2 = tic()
print(t2-t1)

# Now let's loop through everything and find every connection
Dicts = [D3, D4, D5, D6, D7, D8]
for q in range(0, 1):
    Dict_Permutations = permutations([0, 1, 2, 3, 4, 5])
    for A in Dict_Permutations:
    # A = [4, 1, 3, 2, 0, 5]
    # print(A)
        P3 = deepcopy(Dicts[A[0]])
        P4 = deepcopy(Dicts[A[1]])
        P5 = deepcopy(Dicts[A[2]])
        P6 = deepcopy(Dicts[A[3]])
        P7 = deepcopy(Dicts[A[4]])
        P8 = deepcopy(Dicts[A[5]])

        # try:
        for a in P3:
            for b in P4:
                if (str(a)[2:] == str(b)[:2]):
                    P3[a].append(b)
        P3 = {key: list(set(val)) for key, val in P3.items() if val != []}

        P4 = cyclic_match(P4, P5, P3)
        P5 = cyclic_match(P5, P6, P4)
        P6 = cyclic_match(P6, P7, P5)
        P7 = cyclic_match(P7, P8, P6)
        P8 = cyclic_match(P8, P3, P7)

        P3 = cyclic_match_2(P3, P4)
        P4 = cyclic_match_2(P4, P5)
        P5 = cyclic_match_2(P5, P6)
        P6 = cyclic_match_2(P6, P7)
        P7 = cyclic_match_2(P7, P8)
        P8 = cyclic_match_2(P8, P3)

        P3 = cyclic_match_2(P3, P4)
        P4 = cyclic_match_2(P4, P5)
        P5 = cyclic_match_2(P5, P6)
        P6 = cyclic_match_2(P6, P7)
        P7 = cyclic_match_2(P7, P8)
        P8 = cyclic_match_2(P8, P3)

        P3 = cyclic_match_2(P3, P4)
        P4 = cyclic_match_2(P4, P5)
        P5 = cyclic_match_2(P5, P6)
        P6 = cyclic_match_2(P6, P7)
        P7 = cyclic_match_2(P7, P8)
        P8 = cyclic_match_2(P8, P3)

        P3 = cyclic_match_2(P3, P4)
        P4 = cyclic_match_2(P4, P5)
        P5 = cyclic_match_2(P5, P6)
        P6 = cyclic_match_2(P6, P7)
        P7 = cyclic_match_2(P7, P8)
        P8 = cyclic_match_2(P8, P3)

        P3 = cyclic_match_2(P3, P4)
        P4 = cyclic_match_2(P4, P5)
        P5 = cyclic_match_2(P5, P6)
        P6 = cyclic_match_2(P6, P7)
        P7 = cyclic_match_2(P7, P8)
        P8 = cyclic_match_2(P8, P3)

        P3 = cyclic_match_2(P3, P4)
        P4 = cyclic_match_2(P4, P5)
        P5 = cyclic_match_2(P5, P6)
        P6 = cyclic_match_2(P6, P7)
        P7 = cyclic_match_2(P7, P8)
        P8 = cyclic_match_2(P8, P3)


        if len(P8) >= 1:
            print('\n')
            print(A)
            print(P3)
            print(P4)
            print(P5)
            print(P6)
            print(P7)
            print(P8)
            print('\n')




