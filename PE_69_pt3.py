from prime_pat import isprime

product = 1

for i in range(1, 1000000):
    print(i)
    if isprime(i):
        product = product * i
    if product > 1000000:
        product = product / i
        break

print(product)

