from collections import deque

n = int(input())

l = deque([x for x in range(1, n+1)])

while len(l) != 1:
    l.popleft()
    a = l.popleft()
    l.append(a)

print(l[0])