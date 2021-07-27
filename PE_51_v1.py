#Prob 51 prime digit replacement
# def pri_dig_rep(M):
#     n = int
#     prime_list = primes(M)
#     countstop = 7
#     anticountstop = 11-countstop
#     countmax = 0
#     count = 0
#     lowlimit = 1
#     stop = False
#     for n in range(lowlimit,M,2):
#         if prime_list[n]:
#             x = str(n)
#             for i in range(0,len(x)-1):
#                 for j in range(i+1,len(x)):
#                     count = 0
#                     nocount = 0
#                     NN = []
#                     for k in range(0,10):
#                         l = str(k)
#                         NN.append(x[:i]+l+x[i+1:j]+l+x[j+1:])
#                     for l in range(0,10):
#                         if prime_list[int(NN[l])]:
#                             count = count + 1
#                             if count >= countmax:
#                                 print(x)
#                                 countmax = count
#                                 print(countmax)
#                                 if count == countstop:
#                                     stop = True
#                                     break
#                                 else:
#                                     continue
#                             else:
#                                 continue
#                         else:
#                             nocount = nocount + 1
#                             if nocount == anticountstop:
#                                 prime_list[int(NN[l])] = 0
#                                 break
#                         continue
#                     if stop:
#                         break
#                     else:
#                         continue
#                 if stop:
#                     break
#                 else:
#                     continue
#         if stop:
#             break
#         else:
#             continue
#     return n, countmax

# Redo of the above analysis but this will now use primality tests
# def pri_dig_rep(M):
#     n = int
#     r = ''
#     countstop = 8
#     countmax = 0
#     count = 0
#     lowlimit = 1000000001
#     stop = False
#     for n in range(lowlimit,M,2):
#         if fermat_prime(n):
#             x = str(n)
#             print(n)
#             for i in range(0,len(x)-1):
#                 for j in range(i+1,len(x)):
#                     count = 0
#                     NN = []
#                     for k in range(0,10):
#                         l = str(k)
#                         NN.append(x[:i]+l+x[i+1:j]+l+x[j+1:])
#                     for l in range(0,10):
#                         if fermat_prime(int(NN[l])):
#                             count = count + 1
#                             if count >= countmax:
#                                 print(x[:i]+'*'+x[i+1:j]+'*'+x[j+1:], countmax)
#                                 countmax = count
#                                 if count == countstop:
#                                     r = x[:i]+'*'+x[i+1:j]+'*'+x[j+1:]
#                                     stop = True
#                                     break
#                                 else:
#                                     continue
#                             else:
#                                 continue
#                         continue
#                     if stop:
#                         break
#                     else:
#                         continue
#                 if stop:
#                     break
#                 else:
#                     continue
#         if stop:
#             break
#         else:
#             continue
#     return r, countmax
#
# print(pri_dig_rep(10000000000))

# The above second cut has been compreseed and shortened into the below code:

from timeit import default_timer
from prime_pat import isprime, mrprime
t0 = default_timer()

def pri_dig_rep(low, high, counts):
    badcounts = 11-counts
    if low%2 == 0 or high%2 == 0:
        print('High and low inputs must be odd numbers')
        return False
    for n in range(low, high, 2):
        if mrprime(n):
            print(n)
            x = str(n)
            for i in range(0, len(x) - 3):
                for j in range(i + 2, len(x)-1):
                    for m in range(i+1,j):
                        count = 0
                        NN = []
                        if i == 0:
                            r = 1
                        else:
                            r = 0
                        for k in range(r, 10):
                            l = str(k)
                            NN.append(x[:i] + l + x[i + 1:m] + l + x[m+1:j] + l + x[j + 1:])
                        for p in range(0, 10-r):
                            if mrprime(int(NN[p])) == False:
                                count = count + 1
                                if count == badcounts-r:
                                    break
                            if p == 9-r and count < badcounts:
                                print('all done, answer is here:')
                                return NN[0], count-r
print(pri_dig_rep(11,9999999, 8))
t1 = default_timer()

print('Run Time:', t1-t0)