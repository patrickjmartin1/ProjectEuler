def binary(x): #This function converts a number to its binary representation
    y = str(bin(x))[2:]
    return y

def reverse(x): #This number returns the inverse of itself
    y = str(x)[::-1]
    return int(y)

def rltrunc(x): #This function truncates the rightmost letter of a number
    y = str(x)
    y = y[:len(y)-1]
    return int(y)

def lrtrunc(x): #This function truncates the leftmost
    y = str(x)
    y = y[1:]
    return int(y)

def pandigital(x,y): #This function tells us whether or not a number is pandigital starting from one
    for a in range(1, y+1):
        if len(x) != y:
            return False
        if str(a) not in x:
            return False
        elif a == y:
            return True

def pandigital0(x,y): #This function tells us whether or not a number is pandigital starting from zero
    for a in range(0, y+1):
        if len(x) != y+1:
            return False
        if str(a) not in x:
            return False
        elif a == y:
            return True

def pup(x): #this function returns the next largest permutation of a number
    a = str(x)
    for k in range(len(a)-2, -2, -1):
        if k == -1:
            return False
        if a[k] > a[k + 1]:
            continue
        else:
            for i in range(len(a)-1, k, -1):
                if a[k] >= a[i]:
                    continue
                else:
                    a = a[:k] + a[i] + a[k + 1:i] + a[k] + a[i + 1:]
                    f = a[k + 1:]
                    a = a[:k + 1] + f[::-1]
                    return int(a)


def cont_frac(r,n):
    from math import floor
    from fractions import Fraction
    from decimal import Decimal
    r = Fraction(Decimal(str(round(r, 90))))
    a = []
    q = 0
    while q <= n:
        i = floor(r)
        a.append(i)
        f = r-i
        if f == 0:
            return a
        r = pow(f, -1)
        q = q+1
    return a


def convergent(a,n):
    if n >= len(a):
        n = len(a)-1
    if n == 1:
        h = [a[0]]
        k = [1]
        return h,k
    elif n == 2:
        h = [a[0], (a[1]*a[0] + 1)]
        k = [1, a[1]]
        return h,k
    elif n == 3:
        h = [a[0], (a[1]*a[0] + 1), a[2]*(a[1]*a[0] + 1) + a[0]]
        k = [1, a[1], a[2]*a[1] + 1]
        return h,k
    else:
        h = [a[0], (a[1] * a[0] + 1), a[2] * (a[1] * a[0] + 1) + a[0]]
        k = [1, a[1], a[2] * a[1] + 1]
        m = 3
        while m<=n:
            h.append(a[m]*h[m-1] + h[m-2])
            k.append(a[m] * k[m - 1] + k[m - 2])
            m = m+1
        return h,k


def squarecheck(x):
    from math import sqrt
    if sqrt(x) == round(sqrt(x)):
        return True
    else:
        return False

def intcheck(x):
    if round(x) == x:
        return True
    else:
        return False


