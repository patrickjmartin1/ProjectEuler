from prime_pat import isprime

def prime_concat(a, b):
    x = int(str(a) + str(b))
    y = int(str(b) + str(a))
    return x, y

start_prime = [3, 7, 109, 29059]

for i in range(29060, 1000000):
    if isprime(i):
        print(i)
        start_count = 0
        for j in start_prime:
            [x, y] = prime_concat(i, j)
            if isprime(x) and isprime(y):
                start_count = start_count+1
                continue
            else:
                break
        if start_count == 4:
            print("This is the answer {}".format(i))
            break
        else:
            continue
    else:
        continue
