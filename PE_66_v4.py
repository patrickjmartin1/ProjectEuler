# PE_66
# This version (3) will use the bhaskara method of solving the pell equation
# V4 four is the final solution and produces the correct answer. enjoy!

import operator
from pat_lib import squarecheck, intcheck
from timeit import default_timer as t
from math import gcd, sqrt, ceil, floor
from fractions import Fraction
t0 = t()
Dios = {}
sols = [-1, -2, 2, -4, 4]

def bhask_start(D):
    a_high = ceil(sqrt(D))
    a_low = floor(sqrt(D))
    L = abs(pow(a_low, 2) - D)
    H = abs(pow(a_high, 2) - D)
    if L <= H:
        a = a_low
    else:
        a = a_high
    b = 1
    k = pow(a, 2) - D * pow(b, 2)
    return a,b,k

def bhask_iter(D,a,b,k):
    m_check = False
    m_low = floor(sqrt(D))
    m_high = ceil(sqrt(D))
    while m_check == False:
        if m_low <= 0:
            if intcheck((a+b*m_high)/k):
                m = m_high
                m_check = True
            else:
                m_high = m_high+1
                continue
        if abs(pow(m_low,2) - D) < abs(pow(m_high,2) - D):
            if intcheck((a+b*m_low)/k):
                m = m_low
                m_check = True
            else:
                m_low = m_low-1
                continue
        elif abs(pow(m_low,2) - D) > abs(pow(m_high,2) - D):
            if intcheck((a+b*m_high)/k):
                m = m_high
                m_check = True
            else:
                m_high = m_high+1
                continue
        else:
            if intcheck((a+b*m_low)/k):
                m = m_low
                m_check = True
            elif intcheck((a+b*m_high)/k):
                m = m_high
                m_check = True
            else:
                m_low = m_low - 1
                m_high = m_high + 1
                continue
    k_new = Fraction((pow(m, 2) - D), k)
    a_new = Fraction(((a * m) + (D * b)), abs(k))
    b_new = Fraction((a + (b*m)), abs(k))
    return a_new, b_new, k_new, m


def brahma(D, a, b, k):
    a_new = pow(a, 2) + D*pow(b, 2)
    b_new = 2*a*b
    k_new = pow(k, 2)
    return a_new, b_new, k_new


for D in range(1, 1001):
    print(D)
    solved = False
    if squarecheck(D):
        continue
    else:
        a, b, k = bhask_start(D)
        while k != 1:
            a, b, k, m = bhask_iter(D, a, b, k)
            if k == 1:
                Dios[D] = a
                break
            else:
                continue



M = max(Dios.items(), key=operator.itemgetter(1))[0]

t1 = t()
print(M)
print(Dios[M])
print(t1-t0)