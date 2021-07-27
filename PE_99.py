import csv
from math import log2

f_name = 'p099_base_exp.txt'

exp2 = []

with open(f_name, 'r') as f_id:
    reader = csv.reader(f_id, delimiter=',')
    for row in reader:
        print(row[0], row[1])
        b = int(row[0])
        e = int(row[1])
        exp2.append(log2(b) * e)

print(exp2)

max_value = max(exp2)
max_index = exp2.index(max_value)
print(max_index + 1)

