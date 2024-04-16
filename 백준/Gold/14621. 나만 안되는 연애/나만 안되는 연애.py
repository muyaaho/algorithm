import sys
input = sys.stdin.readline

def find_parent(parent, x):
    if x != parent[x]:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
        

n, m = map(int, input().split())
univ = list(input().rstrip().split())
# print(univ)

edges = []
for _ in range(m):
    u, v, d = map(int, input().split())
    edges.append((d, u, v))

edges.sort()

parents = [i for i in range(n+1)]
answer = 0
cnt = 0
for cost, a, b in edges:
    if univ[a-1] == univ[b-1]:
        continue
    if find_parent(parents, a) != find_parent(parents, b):
        union_parent(parents, a, b)
        answer += cost
        cnt += 1
print(-1 if cnt != (n-1) else answer)
