from timeit import default_timer as time
from prime_pat import primes
endnum = int(800)
prime_list = primes(int(1e6))
print('primelist done')
t0 = time()
done = False
for a in range(3, endnum-4, 2):
    if not prime_list[a]:
        continue
    else:
        print(a)
    if a>=7:
        bstart = a+4
    else:
        bstart = 7
    for b in range(bstart,endnum-3, 2):
        if not prime_list[b]:
            continue
        if b >= 109:
            cstart = b + 4
        else:
            cstart = 109
        for c in range(cstart, endnum - 2, 2):
            if not prime_list[c]:
                continue
            if c >= 673:
                dstart = c + 4
            else:
                dstart = 673
            for d in range(dstart, endnum - 1, 2):
                if not prime_list[d]:
                    continue
                for e in range(d+4, endnum, 2):
                    if not prime_list[e]:
                        continue

                    primenums = [a, b, c, d, e]
                    primecats = []
                    for i in range(0,4):
                        for j in range(i+1,5):
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
                            print([a, b, c, d, e])
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
t1 = time()
print(t1-t0)


