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


tc = 1
while True:
    n = int(input())
    
    if n == 0:
        break
    
    parent = [i for i in range(n+1)]
    names = {}
    idx= 1

    for _ in range(n):
        a, b = input().split()
        if a not in names:
            names[a] = idx
            idx += 1
        if b not in names:
            names[b] = idx
            idx += 1
        
        union_parent(parent, names[a], names[b])
    
    print(tc, len(set(parent[1:])))
    tc += 1