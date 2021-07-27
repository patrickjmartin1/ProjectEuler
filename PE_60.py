from timeit import default_timer as time
from prime_pat import primes
endnum = int(1000000)
prime_list = primes(int(1e8))
t0 = time()
done = False
for a in range(3, 4):
    if not prime_list[a]:
        continue
    else:
        print(a)
    if a>=7:
        bstart = a+2
    else:
        bstart = 7
    for b in range(bstart,bstart+1):
        if not prime_list[b]:
            continue
        #else:
            #print(b)
        if b >= 109:
            cstart = b + 2
        else:
            cstart = 109
        for c in range(cstart, cstart+1):
            if not prime_list[c]:
                continue
            if c >= 673:
                dstart = c + 2
            else:
                dstart = 673
            for d in range(dstart, dstart+1):
                if not prime_list[d]:
                    continue
                for e in range(d+2, endnum):
                    if not prime_list[e]:
                        continue

                    primenums = [a, b, c, d, e]
                    primecats = []
                    for i in range(0,3):
                        for j in range(i+1,-1):
                            m = str(primenums[i])
                            n = str(primenums[j])
                            p = int(m+n)
                            q = int(n+m)
                            primecats.extend((p, q))
                    for k in primecats:
                        if prime_list[k] == 0:
                            break
                        elif k == primecats[-1]:
                            done = True
                            print('All Done')
                            print(a+b+c+d+e)
                            print([a,b,c,d,e])
                            break
                    if done:
                        break
                if done:
                    break
            if done:
                break
        if done:
            break
    if done:
        break



