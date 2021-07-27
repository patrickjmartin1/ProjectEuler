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
                    continue
                remsumc = remsumb - c
                for d in range(c+2, int(remsumc/2)+2, 2):
                    if not prime_list[d]:
                        continue
                    e = remsumc - d
                    if not prime_list[e]:
                        continue
                    if e <= d:
                        continue
                    d1 = int(str(a) + str(d))
                    d2 = int(str(d) + str(a))
                    d3 = int(str(d) + str(b))
                    d4 = int(str(b) + str(d))
                    d5 = int(str(d) + str(c))
                    d6 = int(str(c) + str(d))
                    d7 = int(str(e) + str(d))
                    d8 = int(str(d) + str(e))
                    e1 = int(str(a) + str(e))
                    e2 = int(str(e) + str(a))
                    e3 = int(str(e) + str(b))
                    e4 = int(str(b) + str(e))
                    e5 = int(str(e) + str(c))
                    e6 = int(str(c) + str(e))
                    primenums = [a, b, c, d, e]
                    primecats = []

                    if (prime_list[d1] and prime_list[d2] and prime_list[d3] and prime_list[d4] and prime_list[d5] and
                        prime_list[d6]and prime_list[d7]and prime_list[d8]and prime_list[e1]and prime_list[e2]and
                        prime_list[e3]and prime_list[e4]and prime_list[e5]and prime_list[e6]):
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


