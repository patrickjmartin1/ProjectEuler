from timeit import default_timer as time
t0 = time()

with open("p079_keylog.txt","r") as file:
    data = file.read()
nums = data.split('\n')
print(nums)
print(len(nums))
p = []

for i in nums:
    p.append(int(i))

print(p)
# n = []
# for i in range(0,10):
#     for j in p2:
#         if str(i) in str(j):
#             n.append(i)
# n = sorted(list(set(n)))

# for i in range(10000000,1000000000):
#     OK = True
#     for j in p2:
#         for k in j:
#             if str(k) not in str(i):
#                 OK = False
#                 break
            # for l in range(0,len(str(i))):
