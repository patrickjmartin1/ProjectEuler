# V2 of this problem provided the solution. You'll see here that this builds a graph, and the solution is very obvious once you look at the output of the graph.

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
graph = {}
for i in range(0,10):
    graph[str(i)] = []

for i in p:
    j = str(i)
    for k in [0, 1]:
        if j[k+1] in graph[j[k]]:
            continue
        else:
            graph[j[k]].append(j[k+1])
print("Here's the graph:")
print(graph)
# for i in graph:
#     print(i)
#     if '4' in graph[i] or '5' in graph[i]:
#         print('yes')
#     else:
#         print('no')
def generate_edges(graph):
    edges = []
    for node in graph:
        for neighbour in graph[node]:
            edges.append((node, neighbour))

    return edges
print("Here are the edges:")
print(generate_edges(graph))


