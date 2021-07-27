from timeit import default_timer as time
t0 = time()
def sdc(x):
    x = int(x)
    nums = [x]
    open = True
    while open == True:
        sum = 0
        g = str(x)
        for i in g:
            sum = sum + pow(int(i),2)
        x = sum
        nums.append(sum)
        if (x == 1):
            open = False
            return x, nums
        elif x == 89:
            open = False
            return x, nums
        else:
            open = True
            continue

n = int(1e7)
tracker = [0] * (n+1)
en = tracker

for a in range(1,n):
    if tracker[a] == 0:
        print(a)
        [M,N] = sdc(a)
        if M == 89:
            for i in N:
                tracker[i] = 1
                en[i] = 1
        else:
            for i in N:
                tracker[i] = 1
    else:
        continue

print(sum(en))
