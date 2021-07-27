import time
t0 = time.time()
import math
from math import sqrt

#Euler Problem 1

#def sum(n):
#    m = 0
#    i=1
#    while i < n:
#        if i%3 == 0 or i%5 == 0:
#              m = m+i
#              print(m)
#        i = i+1

#sum(1000)

#def sum(j):
#    m = 1
#    n = 2
#    sum1 = 2
#    x=0
#    while x < j:
#        x = m+n
#        m = n
#        n = x
#        if x%2 == 0:
#            sum1 = sum1+x
#            print(sum1)

#sum(4000000)

# Problem 3
#def sum(prime):
#    i = 2
#    j = []
#    y = prime
#    while i <= y:
#        if y == i:
#            j.append(y)
#            break
#        elif y%i == 0:
#            y = y/i
#            k = 2
#            while k <= i+1:
#                if i == k:
#                    j.append(i)
#                    break
#                elif i%k == 0:
#                    break
#                elif k >= i/2:
#                    j.append(i)
#                    break
#                else:
#                    k = k+1
#                    continue
#            i=i+1
#        else :
#            i = i+1
#    print(j)
#sum(600851475143)

# Project Euler #4

# def sum(p):
#     pal = []
#     for r in range(100,p):
#         for q in range(100,p):
#             x = r*q
#             y = str(x)
#             if len(y) == 4:
#                 a, b, c, d = y
#                 if a == d and b == c:
#                     pal.append(x)
#                     continue
#                 else:
#                     continue
#
#             elif len(y) == 5:
#                 a, b, e, c, d = y
#                 if a == d and b == c:
#                     pal.append(x)
#                     continue
#                 else:
#                     continue
#             elif len(y) == 6:
#                 a, b, e, f, c, d = y
#                 if a == d and b == c and e == f:
#                     pal.append(x)
#                     continue
#                 else:
#                     continue
#         continue
#     print(max(pal))
#
# sum(1000)

#Euler #5

# def sum(n):
#     x = 1
#     z = 0
#     for i in range(1, n+1):
#         x = x*i
#         print(x)
#         continue
#     while z == 0:
#         for i in range(1, x):
#             # print(i)
#             for j in range(2,n+1):
#                 if i%j != 0:
#                     break
#                 elif i%j == 0:
#                     continue
#             if j == n and i % j == 0:
#                 z = i
#                 break
#             else:
#                 continue
#     return(z)
# print(sum(20))

#Proj Euler #6

# def squaredif(n):
#     sum = 0
#     sqsum = 0
#     for i in range(1,n+1):
#         sum = sum + i
#         sqsum = sqsum + (i**2)
#         # print(sum)
#         # print(sqsum)
#         continue
#     dif = (sum**2)-sqsum
#     return dif
# print(squaredif(100))

#proj euler #7

# def primecount(n):
#     prime = [];
#     for i in range(2, 10 ** 10):
#         l = len(prime)
#         for j in range(2, 10 ** 10):
#             if i == j:
#                 prime.append(i)
#                 break
#             elif i % j == 0:
#                 break
#             else:
#                 continue
#         if len(prime)==n:
#             break
#         else:
#             continue
#
#     return prime[n-1]
#
# print(primecount(10001))

#Proj Euler #8
# def adjprod(n,m):
#     x = str(n)
#     largest = 0
#     for i in range(0,len(x)-(m+1)):
#         newstring = x[i:i+m]
#         prod = 1
#         for j in range(0,len(newstring)):
#             prod = prod*int(newstring[j])
#             continue
#         if prod > largest:
#              largest = prod
#         else:
#             continue
#     return largest
#
# print(adjprod(7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450,13))

#Euler #9
# Note that this first iteration spelled out below did not solve the problem correctly (did not understand the problem...beers)
# def py():
#     for a in range(1,32):
#         for b in range(1,32):
#             for c in range(1,32):
#                 x = (a**2) + (b**2)+(c**2)
#                 if x == 1000:
#                     return a, b, c, (a*b*c)
#                     break
#                 else:
#                     continue
#             continue
#         continue
#
# print(py())
# import math
# def py():
#     y = 0
#     for a in range(1,500):
#         for b in range(1,500):
#             x = (a ** 2) + (b ** 2)
#             c = math.sqrt(x)
#             if c == int(c) and a + b + c ==1000:
#                 return a,b,c, (a*b*c)
#                 y = 1
#                 break
#             else:
#                 continue
#         if y == 1:
#             break
#         else:
#             continue
#
# print(py())

#Euler 10
# def sumprime(n):
#     prime = [];
#     for i in range(2, n + 1):
#         l = int(math.sqrt(i) + 3)
#         for j in range(2, l):
#             if i % j == 0:
#                 if i == j:
#                     prime.append(i)
#                     break
#                 else:
#                     break
#             elif j == int(math.sqrt(i)):
#                 prime.append(i)
#                 break
#             else:
#                 continue
#         if i == n:
#             break
#         else:
#             print(i)
#             continue
#     return sum(prime)
# print(sumprime(2000000))


# Euler

# def twosum(n):
#     x = 2**n;
#     y = str(x);
#     sum = 0
#     for i in range (0,len(y)):
#         sum = sum + int(y[i])
#         continue
#     return sum
#
# print(twosum(1000))

# Project Euler Work Problem #17
# def lettercount(n):
#     sum = 0
#     for i in range(1, n + 1):
#         num = str(i)
#         print('number', i)
#         if len(num) == 1:
#             sum = sum + onedigit(num)
#             print('length', onedigit(num))
#         if len(num) == 2:
#             sum = sum + twodigit(num)
#             print('length', twodigit(num))
#         if len(num) == 3:
#             sum = sum + threedigit(num)
#             print('length', threedigit(num))
#         if len(num) == 4:
#             sum = sum + 11
#         print('sum', sum)
#         continue
#     return sum
#
# def onedigit(j):
#     length = 0
#     if j == '1' or j == '2' or j == '6':
#         length = 3
#     if j == '3' or j == '7' or j == '8':
#         length = 5
#     if j == '4' or j == '5' or j == '9':
#         length = 4
#     if j == '0':
#         length = 0
#     return length
#
# def twodigit(k):
#     length = 0
#     if k[0] == '1':
#         if k[1] == '0':
#             length = 3
#         if k[1] == '1' or k[1] ==  '2':
#             length  = 6
#         if k[1] == '3' or k[1] == '4' or k[1] == '9' or k[1] == '8':
#             length  = 8
#         if k[1] == '5' or k[1] == '6':
#             length  = 7
#         if k[1] == '7':
#             length  = 9
#     elif k[0] == '2' or k[0] == '3' or k[0] == '8' or k[0] == '9':
#         length = 6 + onedigit(k[1])
#     elif k[0] == '4' or k[0] == '5' or k[0] == '6':
#         length = 5 + onedigit(k[1])
#     elif k[0] == '7':
#         length = 7 + onedigit(k[1])
#     elif k[0] == '0':
#         length =  onedigit(k[1])
#     return length
#
#
#
#
# def threedigit(m):
#     if m[1:3] == '00':
#         length = onedigit(m[0]) + 7
#     else:
#         length = onedigit(m[0]) + 10 + twodigit(m[1:3])
#     return length
#
#
# print(lettercount(1000))

# #Project Euler #20
# def factorial(x):
#     y = 1
#     for i in range(1,x+1):
#         y = y*i
#         continue
#     return y
#
# def facsum(x):
#     thou_num = factorial(x)
#     thou_string = str(thou_num)
#     newsum = 0
#     for i in range(0,len(thou_string)):
#         newsum = newsum + int(thou_string[i])
#         continue
#     return newsum
#
# x = 100
# print(factorial(x))
# print(facsum(x))

#Project Euler # 21 - amicable numbers

# def d(a):
#     b = 1
#     for i in range(2,int((a/2))+1):
#         if a%i == 0:
#             b = b+i
#             continue
#         else:
#             continue
#     return b
#
# def am_ident(x):
#     n = d(x)
#     m = d(n)
#     if m == n:
#         return False
#     if m == x:
#         return True
#     else:
#         return False
#
#
#
# def amicable(x):
#     am_sum = 0
#     for i in range(1,x+1):
#         print(i)
#         if am_ident(i):
#             am_sum = am_sum+i
#             continue
#         else:
#             continue
#     return am_sum
#
# p=10000
# print(amicable(p))


### Project Euler 23: non-abundant sums

# def prop_div_sum(x):
#     num_sum = 1
#     for i in range(2,int(x/2)+1):
#         if x%i == 0:
#             num_sum = num_sum + i
#             continue
#         else:
#             continue
#     return num_sum
#
# def abundant(y):
#     if prop_div_sum(y)>y:
#         return True
#     else:
#         return False
#
# def sorter(n):
#     abundants = []
#     nonabundants = []
#     for i in range(1,n+1):
#         print(i)
#         if abundant(i):
#             abundants.append(i)
#             continue
#         else:
#             nonabundants.append(i)
#             continue
#     return abundants, nonabundants
#
# def summer(z):
#     summer_sum = 6
#     for i in range(4,z+1):
#         print(i)
#         for j in range(1,int(i/2)+2):
#             k = i-j
#             if k in abundants and j in abundants:
#                 break
#             if j<(int(i/2)+1):
#                 continue
#             else:
#                 summer_sum = summer_sum + i
#         continue
#     return summer_sum
#
# upper = 28123
# abundants, nonabundants = sorter(upper)
# print(abundants)
# print(summer(upper))

## Proj Euler #25 1000 bit fibonaci number

# def fibdigit(x):
#     n1 = 1
#     n2 = 1
#     j = 2
#     i=1
#     while i < x:
#         n3 = n2 + n1
#         n1 = n2
#         n2 = n3
#         i = len(str(n3))
#         j = j+1
#     return j
#
#
# print(fibdigit(1000))

#problem 19 counting calendar days

# jan = mar =may = jul = aug = oct = dec = 31
# sep = apr = jun = nov = 30
# feb = 28
#
# n = []
# m=0
# tally = 0
# for i in range(1900,2001):
#     print(i)
#     if i %4 == 0:
#          feb = 29
#          if i == 1900:
#              feb = 28
#          else:
#              feb = 29
#     else:
#          feb = 28
#     cal = [jan, feb, mar, apr, may, jun, jul, aug, sep, oct, nov, dec]
#     for j in range(0,12):
#         for k in range(0,(cal[j])):
#             m = m+1
#             if m%7 == 0:
#                 n.append(1)
#             else:
#                 n.append(0)
#             if i>1900:
#                 if k ==0 and n[m-1]==1:
#                     tally = tally+1
#
# print(len(n))
# print(tally)

#PE #22 names scores
# with open("p022_names.txt","r") as file:
#     data = file.read()
#     names = data.split(',')
#     names2 = sorted(names)
#     cur_total = 0
#     for i in range(0,len(names2)):
#
#         cur_name_sum = 0
#         x = names2[i]
#         print(x)
#         for j in x:
#             if j == '"':
#                 continue
#             else:
#                 cur_name_sum = cur_name_sum + (ord(j)-ord("A")+1)
#
#         cur_total = cur_total+ (cur_name_sum * (i+1))
#
# print(cur_total)

#Proj Euler #24
# def lex(n,m):
#     a = ''
#     j = 1
#     for p in range(0,n+1):
#         a = a + str(p)
#     while j < m:
#         changed = False
#         while changed == False:
#             for k in range(n-1,-2,-1):
#                 if k == -1:
#                     print("Sorry but you've reached the maximum number of permutations")
#                     changed = True
#                     j = m
#                     break
#                 elif int(a[k])>int(a[k+1]):
#                     continue
#                 else:
#                     for i in range(n,k,-1):
#                         if a[k] > a[i]:
#                             continue
#                         else:
#                             a = a[:k] + a[i] + a[k+1:i] + a[k] + a[i+1:]
#                             f = a[k+1:]
#                             a = a[:k+1] + f[::-1]
#                             j=j+1
#                             changed = True
#                             break
#                 break
#     return a
#
# print(lex(9,1000000)
#
# Proj Euler #26

# from decimal import *
# def repeater(d):
#     cymax = 0
#     nummax = 0
#     getcontext().prec = 4000
#     for i in range(3,d+1):
#         print(i)
#         x = Decimal(1)/Decimal(i)
#         y = str(Decimal(x))
#         for j in range(2, 2*i):  # starting string cut
#             found = False
#             for k in range(1, d + 20):  # string cut lengths
#                 y1 = y[j:j+k]
#                 y2 = y[j + k:j +(2 * k)]
#                 y3 = y[j +(2 * k):j +(3 * k)]
#                 if y1 == y2 == y3:
#                     if y1=='0' and y2 == '0' and y3=='0':
#                         continue
#                     if k > cymax:
#                         cymax = k
#                         nummax = i
#                     found = True
#                     break
#                 else:
#                     continue
#             if found:
#                 break
#
#     return nummax, cymax
#
# print(repeater(1000))




# Project Euler #35
# def circ_prime(x):
#     prime_count = 0
#     for i in range(1,x):
#         print(i)
#         if isprime(i):
#             y = str(i)
#             if len(y)==1:
#                 prime_count = prime_count+1
#                 continue
#             else:
#                 for k in range(1,len(y)+1):
#                     z = y[1:] + y[0]
#                     if isprime(int(z)) and k == len(y):
#                         prime_count = prime_count + 1
#                         break
#                     elif isprime(int(z)):
#                         y = z
#                         continue
#                     else:
#                         break
#
#                 continue
#         else:
#             continue
#     return prime_count
#
# print(circ_prime(1000000))

#Problem 39 - Integer right triangles

# def int_tri(p):
#     for i in range(3)

# #Problem 40 Champernowne's Constant
#
# def champ(y):
#
#     x = '0.'
#     for i in range(1,y+1):
#         x = x+str(i)
#     x1 = int(x[2])
#     x2 = int(x[11])
#     x3 = int(x[101])
#     x4 = int(x[1001])
#     x5 = int(x[10001])
#     x6 = int(x[100001])
#     x7 = int(x[1000001])
#
#     z = x1*x2*x3*x4*x5*x6*x7
#     return z
# print(champ(1000000))

# def dubpal(y):
#     allnums = []
#     for i in range(1,y):
#         d1 = str(i)
#         d2 = reverse(d1)
#         if d1 == d2:
#             b1 = str(binary(i))
#             b2 = reverse(b1)
#             if b1 == b2:
#                 allnums.append(i)
#             else:
#                 continue
#         else:
#             continue
#     return sum(allnums)
#
# print(dubpal(1000000))

# Prob 79 - come back to this
# with open("p079_keylog.txt","r") as file:
#      data = file.read()
#      # names = data.split(',')

#print('starting',data,data[0],'done')


#prob 33

# def badcancel(x,y):
#     n = str(x)
#     d = str(y)
#     tf = False
#     if n[1] == '0' and d[1] == '0':
#         tf = False
#     else:
#         for i in [0,1]:
#             for j in [0,1]:
#                 if n[i]==d[j]:
#                     a = int(n[1-i])
#                     b = int(d[1-j])
#                     if b == 0:
#                         tf = False
#                     elif a/b == x/y:
#                         tf = True
#                         break
#                     else:
#                         continue
#     return tf
#
# def prob33():
#     fracsi = 1
#     fracsj = 1
#     for j in range(10,100):
#         for i in range(10,j):
#             if badcancel(i,j):
#                 fracsi = fracsi * i
#                 fracsj = fracsj * j
#     return fracsi, fracsj
#
# print(prob33())



###########################################




############################################
t1 = time.time()
total = t1-t0
print('execution time: ', total)
