## Note that this MUST be run in python 2.7, it will not work in 3.X
from timeit import default_timer as time
t0 = time()
from deuces import Card
from deuces import Evaluator
evaluator = Evaluator()

with open("p054_poker.txt","r") as file:
    data = file.readlines()
    file.close()
p1wins = 0
board = []
for i in data:
    tencards = ''
    tencards = i.split(' ')
    tencards = [s.replace('\n', '') for s in tencards]
    tencards = [s.replace('C', 'c') for s in tencards]
    tencards = [s.replace('H', 'h') for s in tencards]
    tencards = [s.replace('D', 'd') for s in tencards]
    tencards = [s.replace('S', 's') for s in tencards]
    hand1 = tencards[:5]
    hand2 = tencards[5:]
    hand1e = []
    hand2e = []
    for j in hand1:
        hand1e.append(Card.new(j))
    for j in hand2:
        hand2e.append(Card.new(j))
    hand1score = evaluator.evaluate(board, hand1e)
    hand2score = evaluator.evaluate(board, hand2e)
    if hand1score < hand2score:
        p1wins += 1

print(p1wins)
t1 = time()
print(t1-t0)
