from math import sqrt


def calc_from_cont_frac(a):
    m = 0
    while True:
        x = a[-1]
        a = a[:-1]
        # print("x is {}".format(x))
        # print("a is {}".format(a))
        if a == []:
            m = (x + m)
            return m
        else:
            m = 1 / (x + m)


def within_pct(x, y):
    try:
        error = abs((x - round(x)))
    except ZeroDivisionError:
        error = 0
    if error < y:
        print(round(x))
        print('error: {}'.format(error))
        return True, round(x)
    else:
        return False, round(x)

def fill_cont_frac(a, b):
    c = a + b
    while len(c) < 16:
        c = c + b
    return c

print(fill_cont_frac([3], [4, 3, 2]))

soln = calc_from_cont_frac([2, 1, 1, 1, 4, 1, 1, 1, 4])
print(soln)
print(soln ** 2)
if within_pct(soln ** 2, 1e-5):
    print(within_pct(soln ** 2, 1e-5))
else:
    print('nope')

odd_cont_fracs = []

for i in range(1, 100):
    print('start num: {}'.format(i))
    for j in range(1, 10):
        cont_frac_array = fill_cont_frac([i], [j])
        cont_frac_result = calc_from_cont_frac(cont_frac_array)
        cont_frac_square = cont_frac_result ** 2
        wp, num = within_pct(cont_frac_square, 1e-7)
        if wp:
            odd_cont_fracs.append(num)

print(odd_cont_fracs)

for i in range(1, 100):
    print('start num: {}'.format(i))
    for j1 in range(1, 10):
        for j2 in range(1, 10):
            for j3 in range(1, 10):
                cont_frac_array = fill_cont_frac([i], [j1, j2, j3])
                cont_frac_result = calc_from_cont_frac(cont_frac_array)
                cont_frac_square = cont_frac_result ** 2
                wp, num = within_pct(cont_frac_square, 1e-7)
                if wp:
                    odd_cont_fracs.append(num)

for i in range(1, 101):
    print('start num: {}'.format(i))
    for j1 in range(1, 10):
        for j2 in range(1, 10):
            for j3 in range(1, 10):
                for j4 in range(1, 10):
                    for j5 in range(1, 10):


                        cont_frac_array = fill_cont_frac([i], [j1, j2, j3, j4, j5])
                        cont_frac_result = calc_from_cont_frac(cont_frac_array)
                        cont_frac_square = cont_frac_result ** 2
                        wp, num = within_pct(cont_frac_square, 1e-8)
                        if wp:
                            odd_cont_fracs.append(num)

print(odd_cont_fracs)

#
# i = [3]
# j = [1, 1, 1, 1, 6]
# cont_frac_array = fill_cont_frac(i, j)
# print(cont_frac_array)
# cont_frac_result = calc_from_cont_frac(cont_frac_array)
# cont_frac_square = cont_frac_result ** 2
# wp, num = within_pct(cont_frac_square, 1e-5)
# print(wp, num)