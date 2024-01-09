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

n, m, k = map(int, input().split())
arr = list(map(int, input().split()))
parents = [i for i in range(n+1)]
edges = []
for _ in range(m):
    u, v, w = map(int, input().split())
    edges.append((w, u, v))

edges.sort()

for x in arr:
    parents[x] = 0
answer = 0
for w, u, v in edges:
    if find_parent(parents, u) != find_parent(parents, v):
        union_parent(parents, u, v)
        answer += w

print(answer)