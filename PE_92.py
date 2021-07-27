from timeit import default_timer as time
t0 = time()

def sdc(x):
    open = True
    while open == True:
        sum = 0
        g = str(x)
        for i in g:
            sum = sum + int(i)**2
        x = sum
        if (x == 1):
            open = False
            return x
        elif x == 89:
            open = False
            return x
        else:
            open = True
            continue
total = 0
for i in range(1,int((1e6 + 1) )):
    print(i)
    if sdc(i) == 89:
        total +=1
t1 = time()
print(total)
print(t1 - t0)