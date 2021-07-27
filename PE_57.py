from timeit import default_timer
t0= default_timer()

e = [1]
for k in range(1,1005):
    e.extend([2])

def converge(vector, iter_num):

    maxin = iter_num
    n=1
    f = vector[:maxin]
    d = f[maxin-1]

    for i in reversed(f[:maxin-1]):
        n = (i*d)+n
        n,d = d,n

    return d,n
count = 0
for j in range(1,1001):
    k = j+1
    r = converge(e,k)
    if len(str(r[0]))>len(str(r[1])):
        count = count+1
print(count)
t1=default_timer()
print(t1-t0)
