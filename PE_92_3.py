from timeit import default_timer as time
t0 = time()

def sdc1(x):
    x = int(x)
    open = True
    while open == True:
        sum = 0
        g = str(x)
        for i in g:
            sum = sum + pow(int(i),2)
        x = sum
        if (x == 1):
            return x
        elif x == 89:
            return x
        else:
            open = True
            continue

n = int(1e7)
P = n-1
sdcmax = 0
en = 0
for i in str(P):
    sdcmax += pow(int(i),2)
print(sdcmax)
nf = [0] * (sdcmax+1)
for i in range(1,len(nf)):
    if sdc1(i) == 89:
        nf[i] = 1

for a in range(1,n):
    sun = 0
    g = str(a)
    for i in g:
        sun = sun + pow(int(i),2)
    x = sun
    if nf[x] == 1:
        en+=1
        continue
    else:
        continue

t1 = time()
print(en)
print(t1-t0)
