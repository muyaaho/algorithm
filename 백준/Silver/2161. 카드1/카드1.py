from collections import deque

n = int(input())
q = deque(list(range(1, n+1)))

while len(q) > 1:
    print(q.popleft(), end=' ')
    x = q.popleft()
    q.append(x)
print(q[0])