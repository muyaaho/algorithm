from collections import deque
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
ladder, snake = {}, {}

for _ in range(n):
    x, y = map(int, input().split())
    ladder[x] = y

for _ in range(m):
    u, v = map(int, input().split())
    snake[u] = v

q = deque()
q.append(1)

visited = [INF] * 101
visited[1] = 0

while q:
    now = q.popleft()
    
    for i in range(1, 7):
        next = now + i
        if next <= 100:
            while next in ladder or next in snake:
                if next in ladder:
                    next = ladder[next]
                else:
                    next = snake[next]
            
            if visited[now] + 1 < visited[next]:
                visited[next] = visited[now] + 1
                q.append(next)

print(visited[100])
        