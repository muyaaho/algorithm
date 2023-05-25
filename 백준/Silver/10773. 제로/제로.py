from collections import deque

q = deque()
for _ in range(int(input())):
    a = int(input())
    if a != 0:
        q.append(a)
    else:
        q.pop()

print(sum(q))