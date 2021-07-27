i = 2
x = 2

while i <= 7830457:
    x = x*2
    x = int(str(x)[-10:])
    i = i+1

x = int(str(28433*x + 1)[-10:])

print(x)