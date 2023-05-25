from collections import deque
import sys
input = sys.stdin.readline

q = deque()
ans = 0
for _ in range(int(input())):
    a = int(input())
    if a != 0:
        q.append(a)
        ans += a
    else:
        p = q.pop()
        ans -= p

print(ans)