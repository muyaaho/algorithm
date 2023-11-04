import sys
input = sys.stdin.readline

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

n = int(input())

graph = []
for _ in range(int(input())):
    a, b, c = map(int, input().split())
    graph.append((c, a, b))

graph.sort()

parent = [i for i in range(n+1)]

answer = 0
for c, a, b in graph:
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        answer += c
print(answer)