#Proj Euler #24
def lex(n,m):
    a = ''
    j = 1
    for p in range(0,n+1):
        a = a + str(p)
    while j < m:
        changed = False
        while changed == False:
            for k in range(n-1,-2,-1):
                if k == -1:
                    print("Sorry but you've reached the maximum number of permutations")
                    changed = True
                    j = m
                    break
                elif int(a[k])>int(a[k+1]):
                    continue
                else:
                    for i in range(n,k,-1):
                        if a[k] > a[i]:
                            continue
                        else:
                            a = a[:k] + a[i] + a[k+1:i] + a[k] + a[i+1:]
                            f = a[k+1:]
                            a = a[:k+1] + f[::-1]
                            j=j+1
                            changed = True
                            break
                break
    return a

print(lex(9,1000000))