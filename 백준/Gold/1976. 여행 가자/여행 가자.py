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
m = int(input())

parents = [i for i in range(n+1)]
for i in range(n):
    line = list(map(int, input().split()))
    for j, x in enumerate(line):
        if x == 1:
            union_parent(parents, i+1, j+1)

plans = list(map(int, input().split()))

result = True
for i in range(m-1):
    if find_parent(parents, plans[i]) != find_parent(parents, plans[i+1]):
        result = False
        
print("YES" if result else "NO")