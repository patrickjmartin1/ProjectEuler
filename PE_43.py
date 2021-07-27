from pat_lib import pandigital0
from pat_lib import permute_up
# from prime_pat import mrprime, primes
from timeit import default_timer
t0 = default_timer()
seed = int(1023456789)
seedmax = int(9876543210)
pansum = 0
a = seed
nums = []
while a < seedmax+1:
    nums.append(a)
    a = permute_up(a)

print('List Complete')
t2 = default_timer()
print(t2-t0)
for z in nums:
    x = str(z)
    for j in range(1,8):
        y =int( x[j:j+3])
        if j ==1 and y%2==0:
            continue
        elif j ==2 and y%3 ==0:
            continue
        elif j ==3 and y%5 ==0:
            continue
        elif j ==4 and y%7==0:
            continue
        elif j == 5 and y%11==0:
            continue
        elif j == 6 and y%13==0:
            continue
        elif j == 7 and y%17==0:
            print(x)
            pansum = pansum+z
            break
        else:
            break


t1 = default_timer()
print(pansum)
print(t1-t0)






