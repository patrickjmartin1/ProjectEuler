from prime_pat import isprime

for i in range(1000000, 1, -1):
    print(i)
    if isprime(i):
        print("Found it: {}".format(i))
        break

