from collections import deque
import sys
input = sys.stdin.readline
INF = int(1e9)

n = int(input())
arr = [list(input().rstrip()) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

q = deque()
q.append((0, 0))
dist = [[INF] * n for _ in range(n)]
dist[0][0] = 0

while q:
    x, y = q.popleft()
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and dist[nx][ny] == INF:
            if arr[nx][ny] == '1':
                q.appendleft((nx, ny))
                dist[nx][ny] = dist[x][y]
            else:
                q.append((nx, ny))
                dist[nx][ny] = dist[x][y] + 1

print(dist[n-1][n-1])