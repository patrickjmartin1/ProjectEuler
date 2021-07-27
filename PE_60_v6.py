from timeit import default_timer as time
import pickle
endnum = int(1000)
from prime_pat import mrfixed as mr
with open('primefile', 'rb') as fp:
    prime_list = pickle.load(fp)
print('primelist done')
t0 = time()
done = False
maxsum = 5000
for q in range(1451, maxsum, 2):
    print(q)
    for a in range(3, int(q/5)+2, 2):
        if not prime_list[a]:
            continue
        if a == 5:
            continue
        remsuma = q-a
        if a == 3:
            bs = 7
        else:
            bs = a+2
        for b in range(bs,int(remsuma/4)+2, 2):
            if not prime_list[b]:
                continue
            b1 = int(str(a)+str(b))
            b2 = int(str(a)+str(b))
            if not (prime_list[b1] and prime_list[b2]):
                continue
            remsumb = remsuma - b
            for c in range(b+2, int(remsumb/3)+2, 2):
                if not prime_list[c]:
                    continue
                c1 = int(str(a) + str(c))
                c2 = int(str(c) + str(a))
                c3 = int(str(c) + str(b))
                c4 = int(str(b) + str(c))
                if not (prime_list[c1] and prime_list[c2] and prime_list[c3] and prime_list[c4]):
                remsumc = remsumb - c
                for d in range(c+2, int(remsumc/2)+2, 2):
                    if not prime_list[d]:
                        continue
                    e = remsumc - d
                    if not prime_list[e]:
                        continue
                    if e <= d:
                        continue
                    primenums = [a, b, c, d, e]
                    primecats = []
                    for i in range(0,4):
                        for j in range(i+1,5):
                            m = str(primenums[i])
                            n = str(primenums[j])
                            p = int(m+n)
                            r = int(n+m)
                            primecats.extend((p, r))
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
t1 = time()
print(t1-t0)


