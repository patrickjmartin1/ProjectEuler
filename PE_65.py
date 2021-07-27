from timeit import default_timer
t0= default_timer()
e = [2]
for k in range(1,50):
    e.extend([1,2*k,1])
print(e)
maxin = 100
n=1
f = e[:maxin]
d = f[maxin-1]

for i in reversed(f[:maxin-1]):
    n = (i*d)+n
    n,d = d,n

print(d,n)
print(sum(int(i) for i in str(d)))
t1=default_timer()
print(t1-t0)
