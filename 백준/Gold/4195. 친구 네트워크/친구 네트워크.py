import sys
input = sys.stdin.readline

def find_parent(x):
    # print(parent[x])
    if x != parent[x]:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)
    if a != b:
        parent[b] = a
        number[a] += number[b]
    print(number[a]) 
    
for _ in range(int(input())):
    n = int(input())
    parent, number = {}, {}
    
    for _ in range(n):
        a, b = input().rstrip().split()
        if a not in parent:
            parent[a] = a
            number[a] = 1
        if b not in parent:
            parent[b] = b
            number[b] = 1
        
        union_parent(a, b)