from timeit import default_timer as time
from prime_pat import primes
endnum = int(1000)
prime_list = primes(int(1e6))
print('primelist done')
t0 = time()
done = False
for a in range(1, endnum-4, 2):
    if not prime_list[a]:
        continue
    else:
        print(a)
    for b in range(5,endnum-3, 2):
        if not prime_list[b]:
            continue
        for c in range(101, endnum - 2, 2):
            if not prime_list[c]:
                continue
            for d in range(669, endnum - 1, 2):
                if not prime_list[d]:
                    continue
                primenums = [a, b, c, d]
                primecats = []
                for i in range(0,3):
                    for j in range(i+1,4):
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
                        print(a+b+c+d)
                        print([a,b,c,d])
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


