from fractions import Fraction

upper_limit = 3/7
lower_limit = 2/7
frac_bound = 0.99999

r = Fraction(round(upper_limit, 6)).limit_denominator()
print(r)

print(7720448783607203/18014398509481984)

valid_fracs = []

for d in range(0, int(1e6) + 1):
    # Set lower limit for looping to be 1% less than the upperlimit above
    lower_lim = frac_bound * upper_limit * d

    # Loop n from the lower_lim to d
    for n in range(int(lower_lim), d):
        r = Fraction(n/d).limit_denominator()
        if r > upper_limit:
            print(d)
            break
        else:
            valid_fracs.append(r)

valid_fracs.sort()
print(len(valid_fracs))
print(valid_fracs)

"""
Final result from processing: Fraction(428570, 999997)
"""