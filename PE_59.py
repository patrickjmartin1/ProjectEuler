from timeit import default_timer as time
t0 = time()
import textwrap

with open("p059_cipher.txt","r") as file:
    data = file.read()
encoded_string = data.split(',')
encoded = []
for i in encoded_string:
    encoded.append(int(i))

for a in range(97,123):
    for b in range(97,123):
        for c in range(97, 123):
            key = [a, b, c]
            decoded = []
            for i in range(0,len(encoded)):
                if i%3 == 0:
                    D = encoded[i]^key[0]
                    decoded.append(D)
                if i%3 == 1:
                    D = encoded[i]^key[1]
                    decoded.append(D)
                if i%3 == 2:
                    D = encoded[i]^key[2]
                    decoded.append(D)
            decoded_chars = []
            for i in decoded:
                decoded_chars.append(chr(i))
            S = ''.join(decoded_chars)
            if 'thing' in S:
                print(textwrap.fill(S,200))
                print(key)
                for i in key:
                    print(chr(i))
                print(sum(decoded))
                t1 = time()
                print(t1-t0)