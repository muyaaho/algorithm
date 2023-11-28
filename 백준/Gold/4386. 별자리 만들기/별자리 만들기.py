from itertools import combinations
from math import sqrt

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

edges = []
answer = 0

n = int(input())
parent = [i for i in range(n+1)]

coords = [tuple(map(float, input().split())) for _ in range(n)]
m = {x:i for i, x in enumerate(coords)}

for a, b in combinations(coords, 2):
    len = sqrt(abs(a[0]-b[0])**2 + abs(a[1]-b[1])**2)
    edges.append((len, a, b))

edges.sort()
answer = 0

for edge in edges:
    cost, a, b = edge
    if find_parent(parent, m[a]) != find_parent(parent, m[b]):
        union_parent(parent, m[a], m[b])
        answer += cost
        
print(round(answer, 2) if answer - round(answer, 2) < 0.005 else round(answer, 2)+0.01)