A = {1255:1400, 2:[23, 35], 6:'hello'}

B = A


B[1255] = 26
print(B)

B.clear()
B = A
print(B)
print(A)