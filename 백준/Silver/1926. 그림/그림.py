from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def bfs(startx, starty):
    q = deque([(startx, starty)])
    visited[startx][starty] = True
    count = 1
    
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x  +dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and arr[nx][ny] == 1:
                q.append((nx, ny))
                visited[nx][ny] = True
                count += 1
    
    return count    

answer = 0
cnt = 0
visited = [[False] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1 and not visited[i][j]:
            answer = max(answer, bfs(i, j))
            cnt += 1

print(cnt)
print(answer)