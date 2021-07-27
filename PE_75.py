from math import sqrt, gcd


def coprime(x, y):
    if gcd(x, y) == 1:
        return True
    else:
        return False


def is_odd(x):
    odds = [1, 3, 5, 7, 9]
    a = str(x)
    if int(a[-1]) in odds:
        return True
    else:
        return False


def both_odd(x, y):
    if is_odd(x) and is_odd(y):
        return True
    else:
        return False


if __name__ == "__main__":

    len_lim = 1.5e6 + 1
    py_trips = {}

    for m in range(1, int(sqrt(len_lim))+10):
        print(m)

        for k in range(1, int(len_lim)):

            if k * m**2 > len_lim:
                break

            for n in range(1, m):

                if both_odd(m, n):
                    continue

                if not coprime(m, n):
                    continue

                a = k * (m**2 - n**2)
                b = k * 2*m*n
                c = k* (m**2 + n**2)
                total = a+b+c
                if total > len_lim:
                    continue
                else:
                    if total in py_trips.keys():
                        py_trips[total] = py_trips[total] + 1
                    else:
                        py_trips[total] = 1

    unique_triples = 0

    for i in py_trips:
        if py_trips[i] == 1:
            unique_triples = unique_triples + 1

    print(unique_triples)