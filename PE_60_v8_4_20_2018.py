from timeit import default_timer as time
import pickle
from prime_pat import mrfixed as mr
endnum = int(1000)
with open('primefile', 'rb') as fp:
    prime_list = pickle.load(fp)
print('primelist done')
t0 = time()
done = False
maxsum = 5000
print(prime_list[53])

