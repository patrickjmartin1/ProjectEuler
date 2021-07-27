import numpy as np
from itertools import permutations

""" 
Assume that we will have 6-10 in the outer ring for now
"""


def check_valid_entries(x):
    if (1 in x) and (2 in x) and (3 in x) and (4 in x) and (5 in x):
        return True
    else:
        return False


def build_str_and_num(soln, ans):
    soln_short = -(soln[1:])
    full_word = ""
    for indx in range(0, len(soln_short)):
        if indx < 4:
            word = str(int(soln_short[indx])) + str(int(ans[indx]))+ str(int(ans[indx+1]))
        else:
            word = str(int(soln_short[indx])) + str(int(ans[indx])) + str(int(ans[0]))
        full_word = full_word + word

    full_number = int(full_word)
    return full_number




if __name__ == '__main__':
    max_number = []
    # System of equations:
    soe = np.array([[1, 1, 1, 1, 1, 0],
         [1, 1, 0, 0, 0, -1],
         [0, 1, 1, 0, 0, -1],
         [0, 0, 1, 1, 0, -1],
         [0, 0, 0, 1, 1, -1],
         [1, 0, 0, 0, 1, -1]])

    print(soe)

    soe_inv = np.linalg.inv(soe)
    print(soe_inv)

    soln_list = [-10, -9, -8, -7]
    perm = permutations(soln_list)
    valid_count = 0
    for combo in list(perm):
        this_list = list(combo)
        this_list.insert(0, -6)
        this_list.insert(0, 15)
        soln_array = np.transpose(np.array([this_list]))

        # solve the system of equations:
        x = np.matmul(soe_inv, soln_array)

        # First let's check if we have all integers
        x_rounded = np.round(x)
        if np.allclose(x, x_rounded):
            if not np.any(x<=0):
                abcde = np.round(x[:5])
                if check_valid_entries(abcde):
                    valid_count += 1
                    print(this_list)
                    print(x)
                    print("valid count: {}".format(valid_count))

                    print(abcde)

                    this_number = build_str_and_num(soln_array, abcde)
                    max_number.append(this_number)

    print(max(max_number))




