from pat_lib import pup
from timeit import default_timer as ti
t0 = ti()
Data = {}
for i in range(1,10000):
    x = pow(i,3)
    V = [0,0,0,0,0,0,0,0,0,0]
    for j in str(x):
        V[int(j)] = V[int(j)]+1
    try:
        Data[str(V)] = Data[str(V)] + 1
    except KeyError:
        Data[str(V)] = 1
    if Data[str(V)] == 5:
        break

print(V)

for i in range(1,10000):
    x = pow(i,3)
    U = [0,0,0,0,0,0,0,0,0,0]
    for j in str(x):
        U[int(j)] = U[int(j)]+1
    if U == V:
        print(i, x, U)
t1 = ti()
print(t1-t0)