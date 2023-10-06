import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n, m = map(int, input().split())

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
        
parent = [0] * (n+1)
for i in range(1, n+1):
    parent[i] = i

for _ in range(m):
    cmd, a, b = map(int, input().split())
    if cmd == 0:
        union_parent(parent, a, b)
    elif cmd == 1:
        print('YES' if find_parent(parent, a) == find_parent(parent, b) else 'NO')
