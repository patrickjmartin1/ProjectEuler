"""
We'll start over trying to solve this problem - #64
"""
from math import floor, sqrt
import time


def contFrac_eff(x):
    # A more efficient implementation of the continued fraction function
    cf = []
    q = floor(x)
    cf.append(q)
    x = x - q
    i = 0
    while x != 0 and i < 20:
        q = floor(1 / x)
        cf.append(q)
        x = 1 / x - q
        i = i + 1
    return cf


def general_cont_frac(x, n):
    """
    :param x: sqrt of the number we wish to calculate the continued fraction of
    :param n: recursion depth we wish to calculate to (this is a backward-forward calculation
    :return: the full continued fraction, as calculated [a, (b1, b2, b3...bn)]
    """
    return 0


def canonical_cont_frac(S):
    """
    reference:
    https://en.wikipedia.org/wiki/Periodic_continued_fraction

    :param S: The number for which we want to calculate the continued fraction
    :return: the full continued fraction, as calculated [a0, (a1, a2, a3...an)]
    """

    # If x is a perfect square, return 0
    if (sqrt(S) % 1) == 0:
        return 0

    # Otherwise let's proceed
    # Blank list for holding variables

    m = [0]
    d = [1]
    a = [floor(sqrt(S))]

    calculating = True
    while calculating:
        n = len(a) - 1  # Index for grabbing previous values...
        m_n = m[n]
        d_n = d[n]
        a_n = a[n]

        m.append((d_n*a_n) - m_n)
        d.append((S - pow(m[-1], 2))/d_n)
        a.append(floor((a[0] + m[-1])/d[-1]))
        # print(a)

        # Check to see if we have terminated
        if a[-1] == (2 * a[0]):
            calculating = False
            break

        if (m[-1], d[-1], a[-1]) == (m[-2], d[-2], a[-2]):
            calculating = False
            break

    return a


if __name__ == "__main__":
    t_0 = time.time()
    S = 1
    square_count = 0
    even_count = 0
    odd_count = 0

    while True:
        if S <= 10000:
            print("S is: {}".format(S))
            cf = canonical_cont_frac(S)

            if cf == 0:
                square_count += 1
            else:
                period_length = len(cf) - 1
                if period_length % 2 == 0:
                    even_count += 1
                else:
                    odd_count += 1

            print("Continued Fraction is: {} \n".format(cf))
            S = S+1
        else:
            break

    print("Square Count: {}".format(square_count))
    print("Even Count: {}".format(even_count))
    print("Odd Count: {}".format(odd_count))
    print('Check Sum: {}'.format(square_count + even_count + odd_count))

    t_1 = time.time()
    print('Processing time: {} seconds'.format(round(t_1 - t_0, 3)))
