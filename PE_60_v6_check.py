from timeit import default_timer as time
import pickle
endnum = int(1000)
from prime_pat import mrfixed as mr
with open('primefile', 'rb') as fp:
    prime_list = pickle.load(fp)
print('primelist done')
t0 = time()
done = False
maxsum = 800
for q in range(0, maxsum):
    print(q)
    for a in range(3, maxsum-8, 2):
        if not prime_list[a]:
            continue
        remsum = q-a
        for b in range(a+2,remsum-6, 2):
            if not prime_list[b]:
                continue
            remsum = remsum - b
            for c in range(b+2, int(remsum/2)+2, 2):
                if not prime_list[c]:
                    continue
                d = remsum - c

                if not prime_list[d]:
                    continue
                primenums = [a, b, c, d]
                primecats = []
                for i in range(0,3):
                    for j in range(i+1,4):
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
                        print(a+b+c+d)
                        print([a, b, c, d])
                        break

            if done:
                break
        if done:
            break
    if done:
        break
t1 = time()
print(t1-t0)


