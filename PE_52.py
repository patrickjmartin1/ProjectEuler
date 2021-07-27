from timeit import default_timer
t0 = default_timer()
def permultiples(x,y,n):
    for i in range(x,y):
        OK = True
        S = str(i)
        for j in range(1,n+1):
            B = str(i*j)
            if len(B) != len(S):
                break
            for k in S:
                if k in B:
                    continue
                else:
                    OK = False
                    break
            if j ==n and OK:
                return i
            elif OK:
                continue
            else:
                break
a = permultiples(1,1000000,6)
t1 = default_timer()

print(a)
print(t1-t0)
